from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#function defines the http request from the user
def index(request):
    #render html file from templates
    return render(request, "hello/index.html")

def miles(request):
    return HttpResponse("Hello, Miles!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })

    