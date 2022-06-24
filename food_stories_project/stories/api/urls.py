from django.urls import path
from stories.api.views import RecipeAPI, CategoryAPI, RecipeReadUpdateDeleteView


urlpatterns = [
    path('recipes/', RecipeAPI.as_view(), name="api_recipes"),
    path('recipes/<int:pk>/', RecipeReadUpdateDeleteView.as_view(), name="api_recipes"),
    path('categories/', CategoryAPI.as_view(), name="api_categories"),

]