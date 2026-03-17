from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import teacher
from .Forms import teacherform
from .Forms import CreateUserForm
from django.http import HttpResponse


def homepage(request):
    return render(request, 'MyApp/homepage.html')

def register(request):
    context = {}
    return render(request, 'MyApp/register.html', context)
    form1 = CreateUserForm()
    if request.method == "POST":
       form1 = CreateUserForm(request.POST)
       if form1.is_valid():
            form1.save()
            return redirect('my_login')
    context['registerform'] = form1


def my_login(request):
    return render(request, 'MyApp/my_login.html')

def dashboard(request):
    return render(request, 'MyApp/dashboard.html')


# Create your views here.
def index (request):
    context = {}
    teach = teacher.objects.all()
    form = teacherform()
    if request.method == "POST":
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = teacherform(request.POST)
            else:
                Teach = teacher.objects.get(id=pk)
                form = teacherform(request.POST, instance=Teach)
            form.save()
            form = teacherform()

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

 