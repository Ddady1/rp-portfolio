# listings/views.py

from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def about(request):
    return render(request, 'listings/about.html')

def songs_list(request):
    titles = Listing.objects.all()
    return render(request, 'listings/songs_list.html', {'titles': titles})

def contact(request):
    form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})

def song_detail(request, song_id):
    song = Listing.objects.get(id=song_id)
    return render(request,
                  'listings/song_detail.html',
                  {'song': song})

# Create your views here.
