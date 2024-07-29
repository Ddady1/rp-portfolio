# search/views.py

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from search.Tzomet_script import tzomet
from search.Stimatzky_script import stimazky

def search_main(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        tzomet_results = tzomet(book_name)
        stimazky_results = stimazky(book_name)
        #results = 'good book'
        #print(results)
        #return HttpResponse(f'{results}')
        request.session['tzomet_results'] = tzomet_results ##1
        request.session['stimazky_results'] = stimazky_results ##1
        return redirect('search-results') ##1
        #return redirect('search-results', results)
        #return search_results(request, results) stays on the same page
    else:
        return render(request, 'search/search_main.html')

#def search_results(request, book_details):
def search_results(request):
    tzomet_book_details = request.session.get('tzomet_results') ##1
    stimazky_book_details = request.session.get('stimazky_results')
    return render(request, 'search/search_results.html', {'tzomet_book_details': tzomet_book_details, 'stimazky_book_details': stimazky_book_details})




# Create your views here.
