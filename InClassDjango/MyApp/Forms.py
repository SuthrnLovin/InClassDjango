from django import forms
from .models import teacher
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.forms import User


class CreatUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class teacherform(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name', 'Area']
