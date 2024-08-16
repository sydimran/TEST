from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welocme to My First Django Project.</h1>")

def success_Page(request):
    return HttpResponse("<h1>Hey This Is Success Page</h1>")