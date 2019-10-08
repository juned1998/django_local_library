from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance ,Language

#admin.site.register(Author)

class BooksInline(admin.TabularInline):
    model = Book
#DEFUNE the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

#REgister the  admin class associated model
admin.site.register(Author , AuthorAdmin)

#admin.site.register(Book)
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

#admin.site.register(BookInstance)
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('id','book', 'status','borrower' ,'due_back' , 'id' )
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

admin.site.register(Language)
admin.site.register(Genre)
