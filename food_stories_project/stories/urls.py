from django.urls import path
from stories.views import stories, recipes, like_recipe_view, liked_recipes


urlpatterns = [
    path('stories/', stories, name="stories"),
    path('recipes/', recipes, name="recipes"),
    path('like-recipe/<int:id>/', like_recipe_view, name="like_recipe"),
    path('liked-recipes/', liked_recipes, name='liked_recipes')
]