# search/views.py

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from search.Tzomet_script import tzomet

def search_main(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        #results = tzomet(book_name)
        results = 'good book'
        print(results)
        #return HttpResponse(f'{results}')
        return redirect('search-results', results)
    else:
        return render(request, 'search/search_main.html')


def search_results(request, book_details):
    return render(request, 'search/test.html', book_details)




# Create your views here.
