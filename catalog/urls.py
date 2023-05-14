from django.urls import path
from django.views.generic import RedirectView
from .views import home, BookView, BookDetail


urlpatterns = [
    path('', home, name="home"),
    path('books/', BookView.as_view(), name='book-list'),
    path('book/<str:pk>/', BookDetail.as_view() ,name="book-detail")

    
]