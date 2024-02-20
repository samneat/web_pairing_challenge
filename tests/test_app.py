import json

def test_example(web_client):
    response = web_client.get("/users")
    assert response.status_code == 200

def test_get_users(web_client):
    response = web_client.get('/users')
    assert response.status_code == 200
    x = response.data.decode('utf-8') 
    assert json.loads(x) == [
    {"id": 1, "username": "john"},
    {"id": 2, "username": "jane"},
    {"id": 3, "username": "alice"}
]

def test_get_single_user(web_client):
    response = web_client.get('/users/1')
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8')) == {
        "id": 1,
        "username": "john"
    }

def test_post_with_arguments(web_client):
    response = web_client.post('/users', json={'username': 'sam'})
    assert response.status_code == 201
    assert json.loads(response.data.decode('utf-8')) == {"id": 4, "username": "sam"}

def test_put_with_args(web_client):
    response = web_client.put('/users/1', json={"id": 1,"username": "Paul"})
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8')) == {"id": 1, "username": "Paul"}

def test_delete(web_client):
    response = web_client.delete('/users/3')
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8')) == {'message': 'User deleted'}
    response = web_client.get('/users/3')
    assert response.status_code == 404
    assert json.loads(response.data.decode('utf-8')) == {'error': 'User not found'}