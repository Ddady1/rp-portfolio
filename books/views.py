# books/views.py


from django.shortcuts import render
from books.models import Book
from books.Tzomet_script import tzomet


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

def book_index(name):
    book = tzomet(name)
    context = {
        'book': book
    }
    return render(name, 'books/book_index.html', context)

name = book_index('מתג השמדה')
# Create your views here.
