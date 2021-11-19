from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from manager.models import Person


# Create your forms here.

class NewUserForm(UserCreationForm):

    class RegisterForm(ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=PasswordInput)
    email = forms.CharField(widget=EmailInput)

    class Meta:
        model = Person
        fields = ["username", "password", "birthdate", "email"]
