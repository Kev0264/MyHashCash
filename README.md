# Code Challenge: MyHashCash

This is my implementation of the hashcash proof-of-work code challenge.

These commands assume that you have python3 and pip3 installed. To check if python3 is installed, run the following command:
```
python3 -m pip --version
```

To get everything working, run the commands below to setup and run the project. This was created in a Linux environment. If running on Windows, the main difference should only be that instead of `cp` you would use `copy` (unless you're using PowerShell, in which case either works). First we will create a virtual environment *env* then activate it. Then from within the virtual environment we will install the required pip modules, make sure our environment variables are set, and then run the Flask application. Note that using environment variables mainly means that we do not need to run the command `export FLASK_APP=powapp` (or `set FLASK_APP=powapp` in Windows).

```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
cp .env.example .env
flask run
```

---

To run unit tests, run the following:
```
python3 -m pytest
```
---
To test in the brower, issue a GET request to the `/find` endpont like so:
`http://localhost:5000/find?c=iBeat&n=16`

You should get a JSON response of **62073**.

To test the verify endpoint, issue a GET request to:
`http://localhost:5000/verify?c=iBeat&n=16&w=62073`

You should get a response of **true**.