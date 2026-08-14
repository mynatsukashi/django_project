from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from books import models

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

@login_required
def create_post_page(request):
    if request.method == "POST":
        print(request.POST)
        book_title = request.POST["book"]
        author_name = request.POST["author_name"]
        author_surname = request.POST["author_surname"]
        genre_name = request.POST["genres"]
        rating = request.POST["rating"]
        content = request.POST['content']

        author, _ = models.Author.objects.get_or_create(
            name = author_name, surname = author_surname
        )
        genre, _ = models.Genre.objects.get_or_create(genre_name = genre_name)
        book, _ = models.Book.objects.get_or_create(author = author, title = book_title)
        book.genre.add(genre)

        models.Review.objects.create(
            book=book,
            user = request.user,
            rating = rating,
            content = content)
        return redirect("home")
    return render( request, "create.html")

@login_required
def post_comment_section(request, review_id):

    if request.method =="POST":
        print(request.POST)
        user_comment = request.POST.get("comment")
        # Redirects to home page if comment is empty. Without it user will create new comments, but without any context. Not what we are looking for.
        if not user_comment:
            return redirect("home")
        try:
            review = models.Review.objects.get(id=review_id)
        except models.Review.DoesNotExist:
            return redirect("home")

        models.Comment.objects.create(
            user = request.user,
            comment = user_comment,
            review_post = review
        )
        return redirect("home")
    return render(request, "home.html")