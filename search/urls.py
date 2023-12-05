from django.urls import path

from . import views

urlpatterns =[
    path("search", views.search, name="search"),
    path("tag_search", views.tag_search, name="tag_search"),
]