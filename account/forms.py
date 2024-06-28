from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter username"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter password"}))

class RegisterForm(UserCreationForm):
    class Meta:
        model =User
        fields = ["first_name","last_name","email","username","password1","password2"]