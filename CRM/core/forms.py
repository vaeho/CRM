from django import forms
from .models import User, Record
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'company', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'email', 'phone']
