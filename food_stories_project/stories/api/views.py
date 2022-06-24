from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
import django_filters.rest_framework
from rest_framework import filters
from rest_framework.views import APIView
from stories.models import Recipe, Category
from stories.api.serializers import (
    RecipeReadSerializer, RecipeCreateSerializer, 
    CategorySerializer, CategoryCreateSerializer
)

from django.http import JsonResponse


class GenericAPIViewSerializerMixin:

    def get_serializer_class(self):
        return self.serializer_classes[self.request.method] # , self.serializer_classes.get("POST"))
        # if self.request.method == 'GET':
        #     return self.serializer_classes['GET']
        # if self.request.method == 'PUT':
        #     return self.serializer_classes['PUT']
        # if self.request.method == 'PATCH':
        #     return self.serializer_classes['PATCH']
        # return self.serializer_classes['POST']


class RecipeAPI(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = Recipe.objects.all()
    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend,]
    filterset_fields = ['category__title', 'author']
    search_fields = ['title',]
    serializer_classes = {
        'GET': RecipeReadSerializer,
        'POST': RecipeCreateSerializer
    }


class RecipeReadUpdateDeleteView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_classes = {
        'GET': RecipeReadSerializer,
        'PUT': RecipeCreateSerializer,
        'PATCH': RecipeCreateSerializer,
    }


class CategoryAPI(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_classes = {
        'GET': CategorySerializer,
        'POST': CategoryCreateSerializer,
    }


    # def get(self, request, *args, **kwargs):
    #     categories = Category.objects.all()
    #     serializer = CategorySerializer(categories, context={'request': request}, many=True)
    #     return JsonResponse(serializer.data, safe=False)