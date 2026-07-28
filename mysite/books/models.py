from django.db import models
from django.conf import settings


#Models that are related to posts are here

class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    year_of_publishing = models.PositiveSmallIntegerField()
    genre = models.CharField(max_length=30)
    annotation = models.TextField()

    def __str__(self):
        return f"'{self.title}' by {self.author.name} {self.author.surname}"

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    rating = models.DecimalField(max_digits = 1, decimal_places=0)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for '{self.book.title}'"
