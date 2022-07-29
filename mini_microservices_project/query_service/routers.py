from flask import jsonify, request
from flask_cors import cross_origin
from repostories import get_blog_comments, create_blog, create_comment
from app import app


@app.route('/api/posts', methods = ['GET'])
@cross_origin(supports_credentials=True)
def posts():
    blogs = get_blog_comments()
    return jsonify(blogs)


@app.route('/api/events', methods = ['POST'])
@cross_origin(supports_credentials=True)
def events():
    body = request.json
    event_type = body['type']
    if event_type == 'PostCreated':
        create_blog(data=body['data'])
    if event_type == 'CommentCreated':
        create_comment(data=body['data'])
    return jsonify(message='success')