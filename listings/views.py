# listings/views.py

from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing
from listings.forms import BandForm, ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_create(request):
    form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})

def about(request):
    return render(request, 'listings/about.html')

def songs_list(request):
    titles = Listing.objects.all()
    return render(request, 'listings/songs_list.html', {'titles': titles})

def contact(request):
    print('The request methos is:', request.method)
    print('The POST data is:', request.POST)
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via listings Contact us',
                      message=form.cleaned_data['message'],
                      from_email=form.cleaned_data['email'],
                      recipient_list=['admin@song.xyz'])
        return redirect('sent-e')
    else:
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

def email_sent(request):
    return render(request, 'listings/email_sent.html')


# Create your views here.
