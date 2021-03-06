from django import forms
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import (
    UsernameField, AuthenticationForm, UserCreationForm
)
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model, password_validation
from accounts.tasks import send_confirmation_mail

User = get_user_model()


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'email',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }), validators=(validate_password, ))



class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'form-control',
                'placeholder': 'Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'form-control',
                'placeholder': 'Confirm Password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
        return user