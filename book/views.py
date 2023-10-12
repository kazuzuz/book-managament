from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from .models import Review, Book
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


def home(request):
    latest_review_list = Review.objects.filter(created_at__lte=timezone.now()).order_by("-created_at")[ :5]
    
    return render(request, "home.html",{"latest_review_list": latest_review_list})

def detail(request, book_id):
    
    book = get_object_or_404(Book, pk=book_id)
    
    return render(request, "detail.html",{"book": book})


def make_review(request, book_id):
    form = ReviewForm(request.POST)
    try:
        book = get_object_or_404(Book, pk=book_id)
        if form.is_valid():
            review_text = form.cleaned_data['review_text']
            score = form.cleaned_data['score']
            review = Review(book=book, review_text=review_text, score=score)
            review.save()
        else:
            return render(request, "detail.html",{
            "book":book, "form": form
        })
            


    except:
        return render(request, "detail.html",{
            "book":book, "error_message": "正しく入力されていない項目があります。" 
        })
    return HttpResponseRedirect(reverse("book:home"))



#お気に入り登録するための関数
def add_favorite(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    account = request.user
    book.favorite_by.add(account)
    book.save()
    return HttpResponseRedirect(reverse("book:detail", args=[book_id]))

#お気に入り解除するための関数
def delete_favorite(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    account = request.user
    book.favorite_by.remove(account)
    
    return HttpResponseRedirect(reverse("book:detail", args=[book_id]))

#ログイン後に表示するdashboardページ
@login_required(login_url="/login/")
def dashboard(request):
    user = request.user
    favorite_book_list = user.book_set.all()
    
    return render(request, "dashboard.html",{"favorite_book_list": favorite_book_list})