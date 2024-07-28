# search/views.py

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from search.Tzomet_script import tzomet

def search_main(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        results = tzomet(book_name)
        #results = 'good book'
        print(results)
        #return HttpResponse(f'{results}')
        request.session['results'] = results
        return redirect('search-results')
        #return redirect('search-results', results)
        #return search_results(request, results) stays on the same page
    else:
        return render(request, 'search/search_main.html')

#def search_results(request, book_details):
def search_results(request):
    book_details = request.session.get('results')
    return render(request, 'search/search_results.html', {'book_details': book_details})




# Create your views here.
