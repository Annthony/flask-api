from flask import Flask
from hejnote.routes import hejnote_routes

app = Flask(__name__)

hejnote_routes(app)

if __name__ == '__main__':
    app.run()