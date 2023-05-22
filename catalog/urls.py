from django.urls import path
from django.views.generic import RedirectView
from .views import (home, BookView, BookDetail, AuthorListView,
                     AuthorDetailView, LoanedBooksByUserListView,
                     AllBorrowedBooks, RenewBooks, home_view)


urlpatterns = [
    path('', home, name="home"),
    path('books/', BookView.as_view(), name='book-list'),
    path('book/<str:pk>/', BookDetail.as_view() ,name="book-detail"),
    path('authors/', AuthorListView.as_view(), name="authors"),
    path('author/<str:pk>/', AuthorDetailView.as_view(), name="author-detail"),
    path('mybooks/', LoanedBooksByUserListView.as_view(), name="loaned-books" ),
    path('books-borrowed-out/', AllBorrowedBooks.as_view(), name="books-borrowed-out"),
    path('book/<uuid:pk>/renew/', RenewBooks, name="renew-books"),
    




    
]