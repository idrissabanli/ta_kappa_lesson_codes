from django.urls import path
from stories.views import (
    stories, recipes, recipe_detail,  like_recipe_view, 
    liked_recipes, RecipeListView,
    RecipeDetailView, CreateRecipe, UpdateRecipe

)


urlpatterns = [
    path('stories/', stories, name="stories"),
    # path('recipes/<int:id>/', recipe_detail, name="recipe_detail"),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name="recipe_detail"),
    path('create-recipe/', CreateRecipe.as_view(), name="create-recipe"),
    path('update-recipe/<int:pk>/', UpdateRecipe.as_view(), name="update-recipe"),
    path('recipes/', RecipeListView.as_view(), name="recipes"),
    path('like-recipe/<int:id>/', like_recipe_view, name="like_recipe"),
    path('liked-recipes/', liked_recipes, name='liked_recipes')
]