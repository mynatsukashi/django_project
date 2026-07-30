from django.contrib import admin
from books.models import Author, Genre, Book, Review

admin.site.register([Author, Genre, Book, Review])
