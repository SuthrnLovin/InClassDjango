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
            Teach = teacher.objects.get(id=pk)
            Teach.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            Teach = teacher.objects.get(id=pk)
            form = teacherform(instance=Teach) 


    context['form'] = form
    context['teach'] = teach
    
    return render(request, "MyApp/index.html", context)

 