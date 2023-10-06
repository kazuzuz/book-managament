from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "book"
urlpatterns = [
    path("", views.home, name="home"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:book_id>/review", views.make_review, name="make_review"),
    path('register/', views.register, name='register'),
    path("to_register/", views.to_register_page, name="to_register"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('<int:book_id>/add_favorite', views.add_favorite, name="add_favorite"),
    path('<int:book_id>/delete_favorite', views.delete_favorite, name="delete_favorite"),


]