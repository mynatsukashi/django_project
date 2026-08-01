from django.shortcuts import render
from books.models import Review

def home_view(request):
    return render(
        request,
        "home.html",
        {
            "reviews": Review.objects.all()
        }

    )