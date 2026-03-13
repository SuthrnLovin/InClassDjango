from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import teacher
from score.forms import Scoreform

# Create your views here.
def index (request):
    teach = teacher.objects.all()


    return render(request, "MyApp/index.html", {'content': teach})
 