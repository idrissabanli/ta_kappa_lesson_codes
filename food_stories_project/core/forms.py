from django import forms
from core.models import Contact


class ContactForm(forms.ModelForm):
    # full_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
    #             'class': 'form-control',
    #             'placeholder': 'your name',
               
    #         }))

    class Meta:
        model = Contact
        fields = (
            'full_name',
            'email',
            'subject',
            'message',
        )
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name',
               
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject',
                
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
                'rows': 7
                
            }),
        }

