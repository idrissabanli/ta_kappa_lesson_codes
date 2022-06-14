from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login as django_login, logout as django_logout
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from accounts.tokens import account_activation_token

from accounts.forms import LoginForm, RegistrationForm
from accounts.tasks import send_confirmation_mail

User = get_user_model()


class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login_page')

    def form_valid(self, form):
        result = super().form_valid(form)
        send_confirmation_mail(user=self.object, current_site=get_current_site(self.request))
        return result


class ActiveAccountView(View):

    def get(self, request, *args, **kwargs):
        uidb64 = kwargs['uidb64']
        token = kwargs['token']
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Your account activated!')
            return redirect(reverse_lazy('login_page'))
        else:
            messages.warning(request, 'Something went wrong!')
            return redirect(reverse_lazy('login_page'))


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
