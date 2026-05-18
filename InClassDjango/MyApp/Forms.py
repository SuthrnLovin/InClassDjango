from django import forms
from .models import teacher
from .models import Unit
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.forms import User
from .models import AudioFile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AudioUploadForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ['title', 'audio']


class teacherform(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name', 'Area',]


class UnitPdfForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['Title', 'Outline']
