from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from books import models

@login_required
def home_view(request):
    return render(request,"home.html",
        {
            "reviews": models.Review.objects.all()
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

@login_required
def create_post_page(request):
    if request.method == "POST":
        book_title = request.POST["book"]
        author_name = request.POST["author_name"]
        author_surname = request.POST["author_surname"]
        genre_name = request.POST["genres"]
        rating = request.POST["rating"]
        content = request.POST['content']

        author, _ = models.Author.objects.get_or_create(
            name = author_name, surname = author_surname
        )
        book, _ = models.Book.objects.get_or_create(author = author, title = book_title)
        for g in genre_name.split(","):
            genre, _ = models.Genre.objects.get_or_create(genre_name = g.strip())
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