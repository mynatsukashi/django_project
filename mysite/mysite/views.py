from django.shortcuts import render
from books import models

def home_page(request):
    posts = models.Review.objects.all()
    return render(
        request, 
        "home.html",
        {"reviews": posts}
    )