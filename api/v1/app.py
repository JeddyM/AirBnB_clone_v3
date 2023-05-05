#!/usr/bin/python3i
"""The application file"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(arg):
    '''tear down function'''
    storage.close()


@app.errorhandler(404)
def not_found(error):
    '''Handler 404 errors and return SON-formatted 404 status code response'''
    res = jsonify({'error': 'Not found'})
    res.status_code = 404
    return res


if __name__ == '__main__':
    host = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = os.environ.get("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)
