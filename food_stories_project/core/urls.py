from django.urls import path
from core.views import home, contact, ContactView


urlpatterns = [
    path('', home, name="home"),
    path('contact/', ContactView.as_view(), name="contact"),
]