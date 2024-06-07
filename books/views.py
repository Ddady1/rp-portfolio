# books/views.py


from django.shortcuts import render
from books.models import Book
from books.Tzomet_script import tzomet
from books.forms import SearchBook


'''def book_index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/book_index.html', context)


def book_detail(request, pk):
    book = Book.obects.get(pk=pk)
    context = {
        'book': book
    }
    return render(request, 'books/book_detail.html', context)'''

def home_html(request):
    '''if request.method == "GET" and 'book_name' in request.GET:
        book_name = request.GET.get('book_name')
        book = tzomet(book_name)
        context = {
            'book': book
        }
    else:
        context = {
            'book': 'No book was found'
        }'''
    return render(request, 'books/home.html', {})


def book_index(request, name):
    #name = input('Please enter books name:')
    book = tzomet(name)
    print(book)
    context = {
        'book': book
    }
    return render(request, 'books/testh.html', context)
    #print(book)

def bookform(request):
    form = SearchBook()
    return render(request, 'books/home.html', {'form': form})


#name = book_index('מתג השמדה')
# Create your views here.'''
