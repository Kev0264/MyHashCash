#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from flask import url_for

def test_request_contexts(app, client):
    """Activate the request context temporarily and make sure the API endpoints are correct"""
    with app.test_request_context():
        assert url_for('index') == '/'
        assert url_for('find') == '/find'
        assert url_for('verify') == '/verify'

def test_client(app, client):
    """Tests to make sure the web server is working"""
    res = client.get('/')
    assert res.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(res.get_data(as_text=True))

def test_find(app, client):
    """Tests to make sure that the example given in the challenge returns the expected value"""
    res = client.get('/find', query_string={'c': 'iBeat', 'n': 16})
    expected = {'w': 62073}
    assert expected == json.loads(res.get_data(as_text=True))

def test_find_wrong_work_counter(app, client):
    """Change the work counter by one to make sure the test fails as expected"""
    res = client.get('/find', query_string={'c': 'iBeat', 'n': 16})
    expected = {'w': 62072}
    assert expected != json.loads(res.get_data(as_text=True))

def test_find_kevin(app, client):
    """Test using a different string to make sure we get the expected value"""
    res = client.get('/find', query_string={'c': 'Kevin Finkler', 'n': 16})
    expected = {'w': 91045}
    assert expected == json.loads(res.get_data(as_text=True))

def test_find_kevin_wrong_work_counter(app, client):
    """Change the expected value by one to make sure the test fails as expected"""
    res = client.get('/find', query_string={'c': 'Kevin Finkler', 'n': 16})
    expected = {'w': 91046}
    assert expected != json.loads(res.get_data(as_text=True))

def test_verify(app, client):
    """Test that the verify route returns the expected value"""
    res = client.get('/verify', query_string={'c': 'iBeat', 'n': 16, 'w': 62073})
    assert json.loads(res.get_data())

def test_verify_wrong_work_counter(app, client):
    """Change the work counter to make sure that the verification does not succeed as expected"""
    res = client.get('/verify', query_string={'c': 'iBeat', 'n': 16, 'w': 62074})
    assert not json.loads(res.get_data())


