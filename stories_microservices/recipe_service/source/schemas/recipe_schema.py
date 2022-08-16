from marshmallow import fields
from flask_marshmallow.fields import AbsoluteURLFor

from schemas.category_schema import CategorySchema
from models import Recipe
from config.extentions import ma


class RecipeSchema(ma.SQLAlchemyAutoSchema):
    category = fields.Method("get_category")
    author_id = fields.Int(dump_only=True, )
    slug = fields.Str(dump_only=True)
    image = AbsoluteURLFor('uploaded_file', filename='<image>')
    
    class Meta:
        model = Recipe
        include_fk = True
        load_instance = True

        
    def get_category(self, recipe):
        return CategorySchema().dump(recipe.category)