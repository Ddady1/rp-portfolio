#listings/views.py

from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f'''<h1>Hello Bitch!</h1>
                        <p>My favorite bands are:<p>
                        <ul>
                            <li>{bands[0].name}<li>
                            <li>{bands[1].name}<li>
                            <li>{bands[2].name}<li>
                        </ul>
                        ''')

def about(request):
    return HttpResponse('<h1>About Us</h1> <p>We love Python</p>')

def listings(request):
    return HttpResponse('<h1>This is LISTINGS page, BITCH!!</h1>')

def contact(request):
    return HttpResponse('<h2>Dont call us we"ll call you CONTACT page</h2>')

# Create your views here.
