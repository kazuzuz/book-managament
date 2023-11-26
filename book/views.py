from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from .models import Review, Book
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg


def home(request):
    latest_review_list = Review.objects.filter(created_at__lte=timezone.now()).order_by("-created_at")[ :5]
    
    latest_book_list = Book.objects.all().order_by("-pub_date")[ :5]
    
    context ={
        "latest_review_list" :latest_review_list,
        "latest_book_list" : latest_book_list
    }
    
    return render(request, "home.html",context)

def detail(request, book_id):
    user = request.user
    book = get_object_or_404(Book, pk=book_id)
    review_num = Review.objects.filter(book=book).count()
    reviews = Review.objects.filter(book=book)
    if reviews.exists():
        score_ave = reviews.aggregate(avg_score=Avg('score'))['avg_score']
    else:
        score_ave = "--"
    if user.is_authenticated:
        favorite_book_list = user.book_set.all()
        try:
            review = Review.objects.get(book=book, reviewer=user)
            initial_values = {"score" : review.score, "review_text": review.review_text}
        except:
            initial_values = {"score" : None, "review_text": None}
    else:
        initial_values = {"score" : None, "review_text": None}
        favorite_book_list = []
    form = ReviewForm(initial=initial_values)
    
    context ={
        "book": book,
        "favorite_book_list": favorite_book_list,
        "review_num": review_num,
        "score_ave": score_ave,
        "form": form
    }
    return render(request, "detail.html", context)

@login_required
def review(request, book_id):
    form = ReviewForm(request.POST)
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == "POST":
            if form.is_valid():
                review_text = form.cleaned_data['review_text']
                score = form.cleaned_data['score']
                reviewer = request.user
                review, created = Review.objects.update_or_create(
                    reviewer = reviewer,
                    
                    defaults={
                        'book': book,'review_text': review_text,'score': score,'reviewer': reviewer
                    }
                )
                return HttpResponseRedirect(reverse("book:detail", args=[book_id]))
            else:
                return render(request, "detail.html",{
                "book":book, "form": form
            })
            

    return render(request, "review.html", {"book":book} )



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

def search(request):
    pass