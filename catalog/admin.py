from django.contrib import admin
from .models import Book, BookInstance, Author,Language, Genre


# Inline editing of associated records
class BookInstanceInline(admin.TabularInline):
    model = BookInstance

class BookInline(admin.StackedInline):
    model = Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_genre']
    # Inline editing of associated records
    inlines = [BookInstanceInline]
    
    
    

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['book', 'status', 'due_back', 'borrower', 'is_overdue']
    list_filter = ['status', 'due_back']

    # Sectioning the detail view
    fieldsets = (
        (None, {
            'fields':('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields':('status', 'due_back', 'borrower')
        })
    )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # Controlling which fields are displayed and laid out
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

admin.site.register(Language)
admin.site.register(Genre)