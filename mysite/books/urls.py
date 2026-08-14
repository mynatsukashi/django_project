from django.urls import path
from books.views import home_view
from mysite.users import views
from mysite.views import details_page, create_post_page, post_comment_section



urlpatterns = [
    path('', home_view, name = "home"),
    path('review/<int:review_id>/', views.details_page, name ="details"),
]