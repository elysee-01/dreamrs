from django import forms


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
