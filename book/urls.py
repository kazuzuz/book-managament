from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "book"
urlpatterns = [
    path("", views.home, name="home"),
    path("<int:book_id>/", views.detail, name="detail"),
    path("<int:book_id>/review", views.review, name="review"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<int:book_id>/add_favorite', views.add_favorite, name="add_favorite"),
    path('<int:book_id>/delete_favorite', views.delete_favorite, name="delete_favorite"),

]