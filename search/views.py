# search/views.py

from django.shortcuts import render
from django.shortcuts import redirect

def search_main(request):
    return render(request, 'search/search_main.html')



# Create your views here.
