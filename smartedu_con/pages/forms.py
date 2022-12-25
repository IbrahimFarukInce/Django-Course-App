from django import forms
from . models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(label = "",widget = forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : 'Full Name',
        'required' : 'required',
    }))

    email = forms.EmailField(label= '',widget = forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder' : 'Email',
        'required' : 'required',
    }))

    phone = forms.CharField(label='',widget = forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : 'Phone',
        'required' : 'required',
    }))

    message = forms.CharField(label='',widget = forms.Textarea(attrs={
        'class':'form-control',
        'placeholder' : 'Message',
        'required' : 'required',
    }))

    class Meta:
        model = Contact
        fields = ['name','email','phone','message']
        labels = {
            'name':'İsim Soyisim',
            'email':'eposta',
        }