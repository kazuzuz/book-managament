from django.urls import path

from . import views

app_name = "book"
urlpatterns = [
    path("", views.home, name="home"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:book_id>/review", views.make_review, name="make_review"),
]