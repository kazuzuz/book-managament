from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from .models import Review, Book
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from authentication.models import Account
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    latest_review_list = Review.objects.filter(created_at__lte=timezone.now()).order_by("-created_at")[ :5]
    
    return render(request, "home.html",{"latest_review_list": latest_review_list})



class DetailView(generic.DetailView):
    model = Book
    template_name = "detail.html"
    

def make_review(request, book_id):
    try:
        book = get_object_or_404(Book, pk=book_id)
        # TODO FORM　を使う
        review_text = request.POST.get('review_text')
        score = request.POST.get('score')
        review = Review(book=book, review_text=review_text, score=score)
        review.save()
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