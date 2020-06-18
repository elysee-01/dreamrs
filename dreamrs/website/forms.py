from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control w-100',
        'placeholder': 'Enter Message',
        'id': 'message',
        'cols': '30',
        'rows': '9',
    }))

    nom = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your name',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter email address',
    }))

    sujet = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Subject',
    }))

    class Meta:
        model = Contact
        fields = ['message', 'nom', 'email', 'sujet']
