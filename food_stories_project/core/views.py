from django.shortcuts import render
from django.http import HttpResponse


# def home(request):
#     return HttpResponse('Welcome to my page')


def home(request):
    # categories = Ca
    return render(request, 'index.html')