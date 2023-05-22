import datetime
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Book, Author, BookInstance
from .forms import RenewBookForm
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


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
        'number_visits':number_visits,
      
        
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


class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    model = BookInstance
    template_name = 'lonedbookes-by-user.html'
    context_object_name = 'borrowedBooks'


    def get_queryset(self):
        QS = BookInstance.objects.filter(borrower = self.request.user).filter(status__exact = 'o').order_by('due_back')
        return QS
        # return super().get_queryset()

class AllBorrowedBooks(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    model = BookInstance
    template_name = 'librarian/borrowed-books.html'
    permission_required = 'can_mark_returned'

    def get_queryset(self):
        QS = BookInstance.objects.filter(status__exact = 'o')
        return QS

@login_required(login_url='login')
@permission_required('catalog.can_renew', raise_exception=True)
def RenewBooks(request, pk):

    book = get_object_or_404(BookInstance,id=pk)
    form = RenewBookForm()
    proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
    print("*****************************")
    print(proposed_renewal_date)
    form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
    
    

    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book.due_back = form.cleaned_data['renewal_date']
            book.save()
            return HttpResponseRedirect(reverse('books-borrowed-out'))
      
            

    context = {
        'form':form,
        'book':book
    }
    return render(request, 'librarian/renew-books.html', context)

