#!/usr/bin/python3
"""
Create Flask app
"""
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)


if __name__ == '__main__':
    HOST = getenv()
    PORT = int(getenv())
    app.run(host=HOST, port=PORT, threaded=True)
