from flask import Flask
import json

from flask_api.hejnote.routes import hejnote_routes

def setup_test():
    app = Flask(__name__)
    hejnote_routes(app)
    client = app.test_client()
    return app, client


def test_test_route():
    app, client = setup_test()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Hej, I am working!'
    assert response.status_code == 200


def test_get_items():
    app, client = setup_test()
    url = '/api/item'

    response = client.get(url)
    assert response.get_data() == b'[]\n'
    assert response.status_code == 200


def test_get_notes():
    app, client = setup_test()
    url = '/api/note'

    response = client.get(url)
    assert response.get_data() == b'[]\n'
    assert response.status_code == 200


def test_add_note_success():
    app, client = setup_test()
    url = '/api/note'

    mock_request_data = {
        'title': 'Test note title',
        'body': 'Test note body'
    }
    
    response = client.post(url, json = mock_request_data)
    assert response.status_code == 200

    get_response = client.get(url)
    added_note = json.loads(get_response.get_data())[0]
    assert added_note['title'] == mock_request_data['title']
    assert added_note['body'] == mock_request_data['body']


def test_add_note_bad_request():
    app, client = setup_test()
    url = '/api/note'

    mock_request_data = {}
    
    response = client.post(url, json = mock_request_data)
    assert response.status_code == 400


def test_get_todos():
    app, client = setup_test()
    url = '/api/todo'

    response = client.get(url)
    assert response.get_data() == b'[]\n'
    assert response.status_code == 200


def test_add_todo_success():
    app, client = setup_test()
    url = '/api/todo'

    mock_request_data = {
        'title': 'Test todo title',
        'body': 'Test todo body'
    }
    
    response = client.post(url, json = mock_request_data)
    assert response.status_code == 200

    get_response = client.get(url)
    added_todo = json.loads(get_response.get_data())[0]
    assert added_todo['title'] == mock_request_data['title']
    assert added_todo['body'] == mock_request_data['body']


def test_add_todo_bad_request():
    app, client = setup_test()
    url = '/api/todo'

    mock_request_data = {}
    
    response = client.post(url, json = mock_request_data)
    assert response.status_code == 400