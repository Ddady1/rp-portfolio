#listings/views.py

from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})

def about(request):
    return HttpResponse('<h1>About Us</h1> <p>We love Python</p>')

def listings(request):
    titles = Listing.objects.all()
    return HttpResponse(f'''<h1>This is LISTINGS page, BITCH!!</h1>
                        <p>My best song:</p>
                        <ul>
                            <li>{titles[0].title}</li>
                            <li>{titles[1].title}</li>
                            <li>{titles[2].title}</li>
                            <li>{titles[3].title}</li>
                        ''')

def contact(request):
    return HttpResponse('<h2>Dont call us we"ll call you CONTACT page</h2>')

# Create your views here.
