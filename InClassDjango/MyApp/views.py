from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import teacher
from .Forms import teacherform


# Create your views here.
def index (request):
    teach = teacher.objects.all()
    form = teacherform()

    return render(request, "MyApp/index.html", {'content': teach}, {'content': form})
 