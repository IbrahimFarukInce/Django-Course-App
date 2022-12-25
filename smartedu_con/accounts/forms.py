from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username =  forms.CharField(label = "",widget = forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : 'UserName',
        'required' : 'required',
    }))
    password =  forms.CharField(label = "",widget = forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder' : 'Password',
        'required' : 'required',
    }))


class RegisterForm(UserCreationForm):
    firstname =  forms.CharField(label = "",widget = forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : 'First Name',
        'required' : 'required',
    }))

    lastname =  forms.CharField(label = "",widget = forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : 'Last Name',
        'required' : 'required',
    }))

    username =  forms.CharField(label = "",widget = forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : 'UserName',
        'required' : 'required',
    }))

    email =  forms.CharField(label = "",widget = forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder' : 'Email',
        'required' : 'required',
    }))

    password1 =  forms.CharField(label = "",widget = forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder' : 'Password',
        'required' : 'required',
    }))

    password2 =  forms.CharField(label = "",widget = forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder' : 'Re-type Password',
        'required' : 'required',
    }))

    class Meta:
        model = User
        fields = ['firstname','lastname','username','email','password1','password2']


