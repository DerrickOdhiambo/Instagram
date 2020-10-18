from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['email', 'full_name', 'username', 'password1', 'password2']