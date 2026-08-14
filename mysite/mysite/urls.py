"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mysite.views import  home_page
from users.views import signup
from books import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name = "home"),
    path('review/<int:review_id>/', views.details_page, name ="details"),
    path('', include('users.urls')),
    path('create/', views.create_post_page, name="create"),
    path("post-comment/<int:review_id>/", views.post_comment_section, name="post_comment"),
    path('signup/', signup, name="signup")
]
