from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def sayhello(request):
    return HttpResponse('<h1 style="color:red">{“Message”: “Hello World!”}</h1>')


