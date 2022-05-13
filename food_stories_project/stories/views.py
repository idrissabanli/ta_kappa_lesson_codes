from django.shortcuts import render
from stories.models import Recipe


def stories(request):
    return render(request, 'stories.html')

def recipes(request):
    recipe_list = Recipe.objects.all()
    text = 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Numquam, esse, autem sed illum exercitationem quos nemo quo deleniti sequi eaque vero? Dicta perferendis quod culpa in accusamus! Et, minus? Iure.'
    context = {
        'recipes': recipe_list,
        'text': text
    }
    return render(request, 'recipes.html', context)

