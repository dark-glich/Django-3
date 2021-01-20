from django import forms
from .models import Users

class login_form(forms.ModelForm):
    class Meta:
        model = Users
        fields =[
            'first_name',
            'last_name',
            'email',
            'password',
            'terms_condition']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-data', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-data', 'placeholder': 'Enter Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-data', 'placeholder': 'Enter Email ID'}),
            'password': forms.TextInput(attrs={'class': 'form-data', 'placeholder': 'Enter Password'}),
            'terms_condition': forms.CheckboxInput(attrs={'class': "check"})
        }

class signup_form(forms.ModelForm):
    class Meta:
        model = Users
        fields =[
            'email',
            'password']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-data', 'placeholder': 'Enter Email ID'}),
            'password': forms.TextInput(attrs={'class': 'form-data', 'placeholder': 'Enter Password'}),
        }

        