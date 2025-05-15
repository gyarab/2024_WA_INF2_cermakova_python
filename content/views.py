
from django.shortcuts import render
from .models import Book, Genre, Author

def homepage(request):
    books = Book.objects.all()
    return render(request, 'content/homepage.html', {'books': books})

def book(request, id):
    book = Book.objects.get(pk=id)
    return render(request, 'content/book.html', {'book': book})

def genre(request, id):
    genre = Genre.objects.get(pk=id)
    return render(request, 'content/genre.html', {'genre': genre})

def author(request, id):
    author = Author.objects.get(pk=id)
    return render(request, 'content/author.html', {'author': author})
