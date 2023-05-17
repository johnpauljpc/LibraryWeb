from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Book, Author, BookInstance


# Create your views here.
def home(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    bookInstance = BookInstance.objects.all()
    availableBooks = BookInstance.objects.filter(status__exact='a')
    bookCount = books.count()
    number_visits = request.session.get('number_visits', 0)
    request.session['number_visits'] = number_visits + 1
    # request.session['number_visits'] = 0
    # request.session.modified = True
    
    context = {
        'bookCount':bookCount,
        'books':books,
        'authors':authors,
        'bookIns':bookInstance,
        'avCopies': availableBooks,
        'number_visits':number_visits
        
    }
    return render(request, 'index.html', context)

class BookView(ListView):
    model = Book
    template_name = 'book-list.html'
    context_object_name = 'books'
    paginate_by = 2
    queryset = Book.objects.all()#filter(title__icontains='a')[:5] # Get 5 books containing the title war

class BookDetail(DetailView):
    model = Book
    template_name = "book-detail.html"
    context_object_name = "book"

class AuthorListView(ListView):
    model = Author
    template_name = 'authors.html'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
