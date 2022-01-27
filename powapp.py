import hashlib
from flask import Flask, jsonify, request, url_for
import json


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'hello': 'world'})

@app.route("/find")
def find():

    if request.method == 'GET':

        c = request.args.get('c')
        n = request.args.get('n', type=int) # Needs to be an int for the slice below

        w = 0 # work counter

        leadingNBitsFound = False
        maxIterations = 999999999999 # Set arbitrarily large

        # Keep going until we find the digest or until we hit maxIterations
        # (just to keep us from making an infinite loop)
        while not leadingNBitsFound or w < maxIterations:

            cw = c + str(w)

            # Don't need to specify 'UTF-8', but it doesn't hurt
            digest = hashlib.sha256(cw.encode('UTF-8')).hexdigest()

            # Since SHA256 is always 256 bits long, we can pad the zeroes, otherwise it removes them
            # The [2:] removes the '0b' that signifies that it's a binary value
            firstNBits = bin(int(digest, 16))[2:].zfill(256)[:n]

            # If the number of bits that we shopped off the front evaluates to 
            # zero, then we know we have all leading zeros
            intValue = int(firstNBits, 2)

            if intValue == 0:
                leadingNBitsFound = True
                return jsonify(
                    w=w
                )
            else:
                w += 1

@app.route("/verify")
def verify():

    if request.method == 'GET':
        c = request.args.get('c')
        n = request.args.get('n', type=int) # Needs to be an int for the slice below
        w = request.args.get('w')# work counter

        # Basically doing what we did above, but this time we know the w value
        cw = c + w

        digest = hashlib.sha256(cw.encode('UTF-8')).hexdigest()
        firstNBits = bin(int(digest, 16))[2:].zfill(256)[:n]
        intValue = int(firstNBits, 2)
        if intValue == 0:
            return json.dumps(True)
        return json.dumps(False)

with app.test_request_context():
    print(url_for('find'))
    print(url_for('verify'))

if __name__ == "__main__":
    app.run()