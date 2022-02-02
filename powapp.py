#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This is an implementation of the HasCash proof-of-work code challenge
@Author: Kevin Finkler
@Date: 2/2/22
"""

import hashlib
from flask import Flask, jsonify, request, url_for
import json


app = Flask(__name__)

@app.route('/')
def index():
    """The 'home' location returns a simple json object"""
    return jsonify({'hello': 'world'})

@app.route("/find")
def find():
    """Given an arbitrary challenge (c) string and a number of bits (n), this route finds the
    work counter (w) such that the SHA-256 digest of the concatenation of c+w has n leading bits.
    
    Expected parameters of GET request:
    c -- A challenge string
    n -- The number of leading bits to check
    """

    if request.method == 'GET':

        c = request.args.get('c')
        n = request.args.get('n', type=int) # Needs to be an int for the slice below

        w = 0 # work counter

        maxIterations = 999999999999 # Set arbitrarily large

        # Keep going until we find the digest or until we hit maxIterations
        # (just to keep us from making an infinite loop)
        while w < maxIterations:

            cw = c + str(w)

            # Don't need to specify 'UTF-8', but it doesn't hurt
            digest = hashlib.sha256(cw.encode('UTF-8')).hexdigest()

            # Since SHA256 is always 256 bits long, we can pad the zeroes, otherwise it removes them
            # The [2:] removes the '0b' that signifies that it's a binary value
            firstNBits = bin(int(digest, 16))[2:].zfill(256)[:n]

            # If the number of bits that we chopped off the front evaluates to 
            # zero then we know we have all leading zeros
            intValue = int(firstNBits, 2)

            if intValue == 0:
                return jsonify(
                    w=w
                )
            else:
                w += 1

@app.route("/verify")
def verify():
    """Verifies that an arbitrary challenge (c) string and a number of bits (n) produces the expected
    work counter (w) when the SHA-256 digest of the concatenation of c+w has n leading bits.
    
    Expected parameters of GET request:
    c -- A challenge string
    n -- The number of leading bits to check
    w -- The expected work counter
    """

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

"""
The following lines are here to make debugging easier. 
Using the 'flask run' is the preferred way to start a Flask app
"""
#if __name__ == "__main__":
#    app.run()