from config.extentions import db, login_manager
from flask_login import UserMixin
from slugify import slugify


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


class SaveMixin(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    updated_at = db.Column(db.DateTime, server_default=db.func.now())
    created_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(UserMixin, SaveMixin):
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    image = db.Column(db.String(255), nullable=True)
    bio = db.Column(db.Text, nullable=True)


class Category(SaveMixin):
    title = db.Column(db.String(50), nullable=False)


recipies_tags = db.Table('recipies_tags', db.Model.metadata,
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)

class Tag(SaveMixin):
    title = db.Column(db.String(50), nullable=False)
    recipes = db.relationship("Recipe", secondary=recipies_tags, back_populates="tags")


class Recipe(SaveMixin):
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship("Category", backref='recipes')
    tags = db.relationship("Tag", secondary=recipies_tags, back_populates="recipes")
    author_id = db.Column(db.Integer, nullable=False)
    # author = db.relationship("User", backref='stories')
    image = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)


    def save(self):
        self.slug = slugify(self.title)
        return super().save()