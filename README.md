# Code Challenge: MyHashCash

This is my implementation of the hashcash proof-of-work code challenge.

To get everything working, run the following command to setup and run the project. This was created in a Linux environment. If running on Windows, the main difference should only be that instead of `cp` you would use `copy`.

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