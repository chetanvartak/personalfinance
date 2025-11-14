def test_root_endpoint(client):
    res = client.get('/')
    assert res.status_code == 200
    assert 'status' in res.json()
