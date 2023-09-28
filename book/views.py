from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Review, Book

class IndexView(generic.ListView):
    template_name = "home.html"
    context_object_name = "latest_book_list"
    
    def get_queryset(self):
        latest_review_list = Review.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[ :5]
        latest_book_list = []
        for review in latest_review_list:
            b = review.book
            latest_book_list.append(b)
            
        return latest_book_list

class DetailView(generic.DetailView):
    model = Book
    template_name = "detail.html"
        