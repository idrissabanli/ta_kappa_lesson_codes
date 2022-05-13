from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse

from core.forms import ContactForm


# def home(request):
#     return HttpResponse('Welcome to my page')


def home(request):
    # categories = Ca
    return render(request, 'index.html')


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

