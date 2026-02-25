from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index (request):
    now = datetime.now()

    return render(
        request, "MyApp/index.html"
                  {
                      'content' : html_content += "Hello Django! on " + now.strftime("%A, %d %B, %Y at %X")
                  }
                  
                  )

    html_content = "<html><head><title><Hello Django>/title></head><body>"
    html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
    html_content += "</body></html>"

    return HttpResponse("Hello Django")