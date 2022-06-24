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


class RecipeReadUpdateDeleteView(APIView):

    def get(self,request, *args, **kwargs):
        ...
    
    def put(self,request, *args, **kwargs):
        id = kwargs['pk']
        recipe = Recipe.objects.get(id=id)
        recipe_data = request.data
        serializer = RecipeCreateSerializer(data=recipe_data, instance=recipe)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, safe=False, status=200)
    
    def patch(self,request, *args, **kwargs):
        id = kwargs['pk']
        recipe = Recipe.objects.get(id=id)
        recipe_data = request.data
        serializer = RecipeCreateSerializer(data=recipe_data, partial=True, instance=recipe)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, safe=False, status=200)
    
    def delete(self,request, *args, **kwargs):
        ...
    
class CategoryAPI(APIView):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, context={'request': request}, many=True)
        return JsonResponse(serializer.data, safe=False)