import requests
from flask import jsonify, request
from flask_cors import cross_origin
from app import app


@app.route('/api/events', methods = ['POST'])
@cross_origin(supports_credentials=True)
def events():
    body = request.json
    requests.post('http://127.0.0.1:5002/api/events', json=body)
    return jsonify(message='success')