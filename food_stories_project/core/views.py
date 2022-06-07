from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

from core.models import Contact
from core.forms import ContactForm


# def home(request):
#     return HttpResponse('Welcome to my page')


def home(request):
    # categories = Ca
    return render(request, 'index.html')

@login_required
def contact(request):
    form = ContactForm()
    print(request.POST)
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('home'))
    # print('full_name', request.GET.get('email'))

    context = {
        'form': form
    }
    return render(request, 'contact.html', context)



class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Mesajiniz qebul olundu')
        return super().get_success_url()

