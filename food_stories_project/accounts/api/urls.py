from django.urls import path
from accounts.api.views import *


urlpatterns = [
    path('login/', RecipeAPI.as_view(), name="api_login"),

]