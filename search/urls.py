from django.urls import path

from . import views

urlpatterns =[
    path("search", views.search, name="search"),
    path("author_search", views.author_search, name="author_search"),
    path("tag_search", views.tag_search, name="tag_search"),
]