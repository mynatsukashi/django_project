from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from books import models

@login_required
def home_page(request):
    query = request.GET.get('q')

    posts = models.Review.objects.all().order_by('-created_at')

    if query:
        posts = posts.filter(book__title__icontains = query).distinct()
    return render(
        request, 
        "home.html",
        {
            "reviews": posts,
            "query": query,
        }
    )