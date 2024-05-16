# books/views.py


from django.shortcuts import render
from books.models import Book


def book_index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/book_index.html', context)

# Create your views here.
