from django.urls import path
from books.views import home_view


urlpatterns = [
    path('', home_view, name = "home"),
]