from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    books = models.ManyToManyField('Book' )

    def __str__(self):
        return self.name 

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=500)
    author = models.ManyToManyField(Author)
    language = models.ForeignKey(Language, default=1, on_delete = models.SET_DEFAULT)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL)
    ISBN = models.PositiveBigIntegerField()
    availability_status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    

class BookInstance(models.Model):
    unique_id = models.CharField(unique=True, primary_key=True)
    due_back = models.DateField()
    status ='j'
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    imprint = models.CharField(max_length=150)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.unique_id
