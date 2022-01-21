from django.contrib import admin
from book.models import AuthorBooks

# Register your models here.

class AuthorBooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'edition', 'author', 'publication_yr', 'publisher', 'cover']

admin.site.register(AuthorBooks, AuthorBooksAdmin)
