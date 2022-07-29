import requests
from flask import jsonify, request
from flask_cors import cross_origin
from repostories import create_blog, get_blogs
from app import app


@app.route('/api/posts', methods = ['GET', "POST"])
@cross_origin(supports_credentials=True)
def posts():
    if request.method == 'POST':
        title = request.json['title']
        
        
        new_blog = create_blog(title=title)
        post_data = {
            'type': 'PostCreated',
            'data': new_blog
        }
        requests.post('http://127.0.0.1:5003/api/events', json=post_data)
        return jsonify(new_blog), 201
    blogs = get_blogs()
    return jsonify(blogs)




