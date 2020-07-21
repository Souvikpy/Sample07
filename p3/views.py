from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("HELLO world")
    
def home(request):
    return HttpResponse("<h1>Welcome to Home Page<h1>")

def html_demo3(request):
    return render(request,"sample01.html")

def sample2(request):
    return render(request,"directory/sample02.html")

def sample3(request):
    return render(request,"directory/sample03.html", context={'data':"mon",'name':"Dustu"})

def sample4(request):
    vegetable = ['potato','tomato','carrot','cabbage']
    return render(request,"directory/sample04.html",{'vegetable':vegetable})

def sample5(request):
    return render(request,"directory/sample05.html",{'a':10,'b':5})
