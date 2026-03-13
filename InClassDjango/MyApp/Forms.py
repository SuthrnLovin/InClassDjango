from django import forms
from .models import teacher


class ScoreForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name', 'Area']

