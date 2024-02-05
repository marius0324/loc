from django import forms
from .models import Product, AdvUser
from django.contrib.auth.forms import UserCreationForm

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image']


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = AdvUser
        fields = ["username", "email", "password1", "password2"]