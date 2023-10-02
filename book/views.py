from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from .models import Review, Book
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def home(request):
    latest_review_list = Review.objects.filter(created_at__lte=timezone.now()).order_by("-created_at")[ :5]
    
    return render(request, "home.html",{"latest_review_list": latest_review_list})



class DetailView(generic.DetailView):
    model = Book
    template_name = "detail.html"
    

def make_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    review_text = request.POST.get('review_text')
    score = request.POST.get('score')
    review = Review(book=book, review_text=review_text, score=score)
    review.save()
    return HttpResponseRedirect(reverse("book:home"))
    
        