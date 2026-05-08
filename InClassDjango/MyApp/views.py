from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import teacher
from .Forms import teacherform
from .Forms import CreateUserForm
from django.http import HttpResponse
from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from django.http import FileResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from io import BytesIO


def generate_pdf():
    context = {}
    #write text based on what is in the teachr area
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    lines = [('Name:', 'Teaching Area:')]
    teach = teacher.objects.all()
    for teach in teach:
        lines.append((teach.Name, teach.Area))
    field_object = teacher._meta.get_field('Area')
    if field_object == "English":
        lines.append('You picked English')
    table = Table(lines)
    table.wrapOn(p, 300, 300)
    table.drawOn(p, 0, 750)
    p.showPage()
    p.save()
    buffer.seek(0)
    context['field_object'] = field_object
    return buffer


def report(request):
    pdf_file =  staticfiles_storage.path("PracticePDF.pdf")
    try:
        merger = PdfWriter()
        input1 = PdfReader(generate_pdf())
        input2 = PdfReader(pdf_file, "rb")
        merger.append(input1)
        merger.append(input2)
        buffer = BytesIO()
        merger.write(buffer)
        buffer.seek(0)
        response = FileResponse(buffer, as_attachment=True, filename="hello.pdf")
    except FileNotFoundError:
        response = FileResponse(generate_pdf(), as_attachment=True, filename="no.pdf")

    

    return response

def register(request):
    context = {}
    form1 = CreateUserForm()
    if request.method == "POST":
       form1 = CreateUserForm(request.POST)
       if form1.is_valid():
            form1.save()
            return redirect('my_login')
    context['registerform'] = form1
    return render(request, 'MyApp/register.html', context)



def my_login(request):
    return render(request, 'MyApp/my_login.html')

def dashboard(request):
    return render(request, 'MyApp/dashboard.html')


# Create your views here.
def index (request):
    context = {}
    teach = teacher.objects.all()
    form = teacherform()
    field_object = teacher._meta.get_field('Area')
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
    context['field_object'] = field_object
    
    return render(request, "MyApp/index.html", context)

 