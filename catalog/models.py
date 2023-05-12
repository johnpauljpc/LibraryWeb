from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField('Died', null=True, blank=True)
    # books = models.ManyToManyField('Book' )
    

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}' 

class Genre(models.Model):
    name = models.CharField(max_length=100, help_text = "enter a book genre(e.g. Science, Inspirational etc)")

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    # author = models.ManyToManyField(Author)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    language = models.ForeignKey(Language,  on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    ISBN = models.CharField('ISBN', max_length=13, unique=True,  help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    # availability_status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('bool-detail', args=[str(self.id)])
    

class BookInstance(models.Model):
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=150)
    due_back = models.DateField(blank=True, null=True)
    status =models.CharField(max_length=1, choices=LOAN_STATUS, default='m',help_text='Book availability',)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} {self.book.title}'
    
    def get_absolute_url(self):
        return reverse('bookinstance-detail', args=[str(self.id)])
