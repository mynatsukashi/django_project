from django.db import models
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


#Models that are related to posts are here

class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Genre(models.Model):
    genre_name = models.CharField(max_length=30, unique = True)

    def __str__(self):
        return self.genre_name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f"'{self.title}' by {self.author.name} {self.author.surname}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    rating = models.IntegerField(
        default = 5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def stars(self):
            return "★" * self.rating + "☆" * (5 - self.rating)
    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['user', 'book'], name='unique_review_per_user_per_book')
        ]
    
    def __str__(self):
        return f"Review by {self.user.username} for '{self.book.title}'"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    review_post = models.ForeignKey(Review, related_name = "comments", on_delete = models.CASCADE)
    comment = models.TextField()
    

    def __str__(self):
        return f"{self.comment}"


    