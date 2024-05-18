# books/views.py


from django.shortcuts import render
from books.models import Book


def book_index(request):
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
    return render(request, 'books/book_detail.html', context)

# Create your views here.
