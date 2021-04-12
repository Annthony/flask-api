from flask import Flask
import json

from hejnote.routes import hejnote_routes

def test_test_route():
    app = Flask(__name__)
    hejnote_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Hej, I am working!'
    assert response.status_code == 200