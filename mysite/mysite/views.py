from django.shortcuts import render, redirect
from books import models

def home_page(request):
    posts = models.Review.objects.all().order_by('-created_at')
    return render(
        request, 
        "home.html",
        {"reviews": posts}
    )

def details_page(request,review_id):
    try:
        review = models.Review.objects.get(id=review_id)
    except models.Review.DoesNotExist:
        return redirect("home")

    comments = models.Comment.objects.filter(review_post= review_id)

    context = {
        "review": review,
        "comments": comments,
    }
    return render(request, "details.html", context)

def category_page(request):
    return render(request, "category.html")