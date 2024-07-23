# search/views.py

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from search.Tzomet_script import tzomet

def search_main(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        results = tzomet(book_name)
        print(results)
    return HttpResponse(f'{results}')
    #return redirect(request, 'search/test.html', {'results': results})



# Create your views here.
