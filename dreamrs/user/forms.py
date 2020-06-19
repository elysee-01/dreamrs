from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile



class LoginForm(forms.Form):
    '''
        Formulaire de connexion
    '''
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Username',
        }
    ))
    
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
        }
    ))



class RegisterForm(UserCreationForm):
    '''
        Formulaire d'inscription
    '''
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Nom',
            'class': 'width-2',
        }
    ))

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Prenom',
            'class': 'width-2',
        }
    ))

    adresse = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'Adresse',
            'class': 'width-2',
        }
    ))

    website = forms.URLField(required=False, widget=forms.URLInput(
        attrs={
            'placeholder':'Website',
            'class': 'width-2',
        }
    ))
    
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Nom d\' utilisateur',
        }
    ))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Email',
        }
    ))

    photo = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={
            'placeholder': 'Avatar',
            'id': 'file',
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'Mot de passe',
            'class': 'width-2',
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'Confirmer le mot de passe',
            'class': 'width-2',
        }
    ))

    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'placeholder':'Parlez nous un peut de vous',
            'rows': '6',
        }
    ))

    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = (
            'last_name', 
            'first_name',
            'adresse', 
            'website',
            'username',
            'email',
            'photo', 
            'password1', 
            'password2',
            'description'
        )
