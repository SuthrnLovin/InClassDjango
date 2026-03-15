from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import teacher
from .Forms import teacherform


# Create your views here.
def index (request):
    context = {}
    teach = teacher.objects.all()
    form = teacherform()
    context['form'] = form
    context['teach'] = teach
   

    return render(request, "MyApp/index.html", context)

 