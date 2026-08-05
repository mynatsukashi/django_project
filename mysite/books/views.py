from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from books.models import Author, Book, Genre, Review

@login_required
def home_view(request):
    return render(request,"home.html",
        {
            "reviews": Review.objects.all()
        }

    )

