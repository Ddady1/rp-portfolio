#listings/views.py

from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello Bitch!</h1>')

def about(request):
    return HttpResponse('<h1>About Us</h1> <p>We love Python</p>')

# Create your views here.
