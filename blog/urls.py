"""lipikoron URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("lipikar/<name>/", views.getAuthor, name = "author"),
    path("lipi/<int:id>/", views.getSingle, name = "single_post"),
    path("lipi/like", views.like, name="postlike"),
    path("lipi/<int:post_id>/report/", views.report, name="report"),
    path("category/<slug>/", views.getCategory, name = "category"),
    path("dashboard/", views.getDashboard, name = "dashboard"),
    path("create/", views.getCreate, name = "create"),
    path("update/<int:id>/", views.getUpdate, name = "update"),
    path("delete/<int:id>/", views.getDelete, name = "delete"),
    path("lipi/bookmark/", views.bookmark, name="bookmark"),
    path("search/", views.getSearch, name="search"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),


]
