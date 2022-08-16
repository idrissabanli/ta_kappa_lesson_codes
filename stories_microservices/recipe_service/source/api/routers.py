from flask import request, send_from_directory
from marshmallow import ValidationError
from app import app
from utils import save_image
from models import Recipe
from schemas.recipe_schema import RecipeSchema
from flask_jwt_extended import jwt_required, get_jwt_identity


@app.route('/api/recipes', methods=['GET', 'POST'])
@jwt_required()
def recipes():
    if request.method == "POST":
        image = request.files.get('image', None)
        if image:
            image_path = save_image(image)
        recipe_data = dict(request.form) or request.get_json(silent=True) or dict()
        recipe_data['image'] = image_path
        try:
            recipe = RecipeSchema().load(recipe_data)
            recipe.author_id = get_jwt_identity()
            recipe.save()
        except ValidationError as err:
            return err.messages, 400
        return RecipeSchema().jsonify(recipe), 201
    recipes = Recipe.query.all()
    return RecipeSchema().jsonify(recipes, many=True), 200


@app.route('/media/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['MEDIA_ROOT'], filename)