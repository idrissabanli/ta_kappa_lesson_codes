from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from stories.models import Recipe, Category


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


def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    categories = Category.objects.all()
    context = {
        'recipe': recipe,
        'categories': categories
    }
    return render(request, 'single.html', context)


class RecipeListView(ListView):
    model = Recipe
    paginate_by = 1
    context_object_name = 'recipes'
    template_name = 'recipes.html'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'single.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) # context = { 'recipe': recipe }
        context['categories'] = Category.objects.all()
        return context


def like_recipe_view(request, id):
    request.session['liked_recipes'] = f"{request.session.get('liked_recipes', '')}{id} " # '1,2,3,4'
    print(request.session['liked_recipes'])
    messages.success(request, 'Recipe like edildi!')
    return redirect(reverse_lazy('recipes'))


def liked_recipes(request):
    l_recipes = list(map(int, request.session.get('liked_recipes', '').split())) 
    recipe_list = Recipe.objects.filter(id__in=l_recipes)
    context = {
        'recipes': recipe_list,
    }
    return render(request, 'recipes.html', context)
