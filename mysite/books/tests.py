from django.test import TestCase
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from .models import Review, Book, Genre, Author

# Create your tests here.

class ReviewModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username = "testuser", password = "123test")
        self.author = Author.objects.create(name = "John", surname = "Johnson")
        self.genre = Genre.objects.create(genre_name = "Fantasy")
        self.book= Book.objects.create(author= self.author, title = "When sun rises")
        self.book.genre.add(self.genre)
        self.review = Review.objects.create(user=self.user, book = self.book, rating = 5, content="Good") 

    def test_duplicate_review_same_user_same_book_error(self):
        with self.assertRaises(IntegrityError):
            Review.objects.create(
                user = self.user,
                book = self.book,
                rating = 3,
                content = "Another review"
            )
