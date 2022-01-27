
import json

def test_client(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(res.get_data(as_text=True))

def test_find(app, client):
    res = client.get('/find', query_string={'c': 'iBeat', 'n': 16})
    expected = {'w': 62073}
    assert expected == json.loads(res.get_data(as_text=True))

def test_find_wrong_work_counter(app, client):
    res = client.get('/find', query_string={'c': 'iBeat', 'n': 16})
    expected = {'w': 62072}
    assert expected != json.loads(res.get_data(as_text=True))

def test_find_kevin(app, client):
    res = client.get('/find', query_string={'c': 'Kevin Finkler', 'n': 16})
    expected = {'w': 91045}
    assert expected == json.loads(res.get_data(as_text=True))

def test_find_kevin_wrong_work_counter(app, client):
    res = client.get('/find', query_string={'c': 'Kevin Finkler', 'n': 16})
    expected = {'w': 91040}
    assert expected != json.loads(res.get_data(as_text=True))

def test_verify(app, client):
    res = client.get('/verify', query_string={'c': 'iBeat', 'n': 16, 'w': 62073})
    assert json.loads(res.get_data())

def test_verify_wrong_work_counter(app, client):
    res = client.get('/verify', query_string={'c': 'iBeat', 'n': 16, 'w': 62074})
    assert not json.loads(res.get_data())


