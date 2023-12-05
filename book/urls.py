from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "book"
urlpatterns = [
    path("", views.home, name="home"),
    path("<int:book_id>/", views.detail, name="detail"),
    path("<int:book_id>/review", views.review, name="review"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/books/<int:book_id>/add_favorite', views.AddFavoriteView.as_view(), name="add_favorite"),
    path('api/books/<int:book_id>/delete_favorite', views.DeleteFavoriteView.as_view(), name="delete_favorite"),

]