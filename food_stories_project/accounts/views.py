from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login as django_login, logout as django_logout
from django.contrib.auth import get_user_model

from accounts.forms import LoginForm
User = get_user_model()

# http://localhost:8000/accounts/login/?next=/idris/
def login_page(request):
    next_page = request.GET.get('next', '/') # '/accounts/profile/'
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password']) 
            if user:
                django_login(request, user)    
                messages.add_message(request, messages.SUCCESS, 'Ugurla login oldunuz')
                return redirect(next_page)
            else:
                messages.add_message(request, messages.ERROR, 'Username ve ya password sehvdir!')
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logout_page(request):
    django_logout(request)
    messages.add_message(request, messages.SUCCESS, 'Log out oldunuz!')
    return redirect(reverse_lazy('login_page'))


@login_required
def user_profile(request):
    # user = User.objects.get(id=request.user.id)
    # context = {
    #     'user': 
    # }
    return render(request, 'user-profile.html',)
