from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import teacher
from .forms import ScoreForm


# Create your views here.
def index (request):
    teach = teacher.objects.all()
    context = {}
    form = ScoreForm()
    context['form'] = form
    context['teach'] = teach

    return render(request, "MyApp/index.html", context)
 