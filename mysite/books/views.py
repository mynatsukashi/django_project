from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from books.models import Author, Book, Genre, Review

@login_required
def home_view(request):
    if request.method == "POST":
       post = Review.objects.create(
            user = request.user,
            book=request.POST.get("book"),
            author_name = request.POST.get("author_name"),
            author_surname = request.POST.get("author_surname"),
            genres = request.POST.get("genres"),
            rating = request.POST.get("rating"),
            content = request.POST.get("content")
        )
    return render(
        request,
        "home.html",
        {
            "reviews": Review.objects.all()
        }

    )