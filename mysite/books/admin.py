from django.contrib import admin
from books.models import Author, Genre, Book, Review, Comment

admin.site.register([Author, Genre, Book, Review, Comment])
