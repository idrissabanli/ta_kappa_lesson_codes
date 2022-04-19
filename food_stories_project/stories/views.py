from django.shortcuts import render
from stories.models import Recipe


def stories(request):
    return render(request, 'stories.html')

def recipes(request):
    recipe_list = Recipe.objects.all()
    context = {
        'recipes': recipe_list
    }
    return render(request, 'recipes.html', context)
