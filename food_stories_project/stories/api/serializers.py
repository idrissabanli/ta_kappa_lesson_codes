from rest_framework import serializers
from drf_yasg.utils import swagger_serializer_method
from stories.models import Recipe, Category



class RecipeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'short_description',
            'image',
            'category',
            'created_at',
            'updated_at',
        )


class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'image'
        )


class CategorySerializer(serializers.ModelSerializer):
    recipes = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'image',
            'recipes'
        )
    
    @swagger_serializer_method(serializer_or_field=RecipeCategorySerializer(many=True))
    def get_recipes(self, obj):
        serializer = RecipeCategorySerializer(obj.recipes.all(), context=self.context, many=True)
        return serializer.data


class RecipeReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'short_description',
            'image',
            'author',
            'category',
            'created_at',
            'updated_at',
        )


class RecipeCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'short_description',
            'image',
            'author',
            'category',
            'created_at',
            'updated_at',
        )
    
    def validate(self, data):
        request = self.context['request']
        data['author'] = request.user
        return super().validate(data)