from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance

# Create your views here.
def home(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    bookInstance = BookInstance.objects.all()
    availableBooks = BookInstance.objects.filter(status__exact='a')
    bookCount = books.count()
    
    context = {
        'bookCount':bookCount,
        'books':books,
        'authors':authors,
        'bookIns':bookInstance,
        'avCopies': availableBooks
        
    }
    return render(request, 'index.html', context)