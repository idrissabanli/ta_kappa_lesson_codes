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
        return jsonify(new_blog), 201
    blogs = get_blogs()
    return jsonify(blogs)