from django import forms
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UsernameField

class LoginForm(forms.Form):
    username = UsernameField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'email',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }), validators=(validate_password, ))