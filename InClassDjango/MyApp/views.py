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
    if request.method == "POST":
        if 'save' in request.POST:
            form = teacherform(request.POST)
            form.save()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            teach = form.objects.get(id=pk)
            teach.delete()


    context['form'] = form
    context['teach'] = teach
    
    return render(request, "MyApp/index.html", context)

 