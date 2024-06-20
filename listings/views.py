# listings/views.py

from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def about(request):
    return render(request, 'listings/about.html')

def listings(request):
    titles = Listing.objects.all()
    return render(request, 'listings/listings.html', {'titles': titles})

def contact(request):
    return render(request, 'listings/contact.html')

def band_detail(request, id):
    return render(request,
                  'listings/band_detail.html',
                  {'id': id})

# Create your views here.
