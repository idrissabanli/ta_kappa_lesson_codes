from rest_framework.views import APIView
from stories.models import Recipe, Category
from stories.api.serializers import (
    RecipeReadSerializer, RecipeCreateSerializer, 
    CategorySerializer
)

from django.http import JsonResponse


class RecipeAPI(APIView):

    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        serializer = RecipeReadSerializer(recipes, context={'request': request}, many=True)
        # recipes_dict = []
        # for recipe in recipes:
        #     recipes_dict.append({
        #         'id': recipe.id,
        #         'title': recipe.title,
        #         'content': recipe.content
        #     })
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        form_data = request.data
        serializer = RecipeCreateSerializer(data=form_data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=201)
        return JsonResponse(serializer.errors, safe=False, status=400)

    
class CategoryAPI(APIView):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, context={'request': request}, many=True)
        return JsonResponse(serializer.data, safe=False)