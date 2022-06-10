from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  (
    ListView, DetailView, TemplateView, CreateView, UpdateView
)
from django.urls import reverse_lazy
from stories.models import Recipe, Category
from stories.forms import RecipeForm



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
    paginate_by = 5
    context_object_name = 'recipes'
    template_name = 'recipes.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        cat_id = self.request.GET.get('cat') # cat=1
        if cat_id:
            queryset = queryset.filter(category__id=cat_id)
        return queryset


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'single.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) # context = { 'recipe': recipe }
        context['categories'] = Category.objects.all()
        return context



class CreateRecipe(LoginRequiredMixin, CreateView):
    template_name = 'create_recipe.html'
    form_class = RecipeForm
    # success_url = '/'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Yeni resept yaradildi')
        return super().get_success_url()

    def form_valid(self, form):
        # recipe = form.save(commit=False)
        # recipe.author = self.request.user
        # recipe.save()
        # return HttpResponseRedirect(self.get_success_url())
        form.instance.author = self.request.user
        return super().form_valid(form=form)

    

class UpdateRecipe(LoginRequiredMixin, UpdateView):
    template_name = 'create_recipe.html'
    model = Recipe
    form_class = RecipeForm
    # success_url = '/'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Yeni resept update olundu')
        return super().get_success_url()



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
