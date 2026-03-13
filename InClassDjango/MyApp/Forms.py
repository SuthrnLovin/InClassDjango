from django import forms
from score.models import Score

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        feilds = ['name', 'vale']
