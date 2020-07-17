from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("HELLO world")
    
def home(request):
    return HttpResponse("<h1>Welcome to Home Page<h1>")

def html_demo3(request):
    return render(request,"sample01.html")