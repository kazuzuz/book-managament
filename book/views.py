from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from .models import Review, Book
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from authentication.models import Account
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    latest_review_list = Review.objects.filter(created_at__lte=timezone.now()).order_by("-created_at")[ :5]
    
    return render(request, "home.html",{"latest_review_list": latest_review_list})



class DetailView(generic.DetailView):
    model = Book
    template_name = "detail.html"
    

def make_review(request, book_id):
    try:
        book = get_object_or_404(Book, pk=book_id)
        review_text = request.POST.get('review_text')
        score = request.POST.get('score')
        review = Review(book=book, review_text=review_text, score=score)
        review.save()
    except:
        return render(request, "detail.html",{
            "book":book, "error_message": "正しく入力されていない項目があります。" 
        })
    return HttpResponseRedirect(reverse("book:home"))


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = Account.objects.create_user(email=email, password=password)
        user.save()
        
        return HttpResponseRedirect(reverse("book:home"))
    
    return render(request, reverse("book:register"))        


def to_register_page(request):
    return render(request, "register.html" )


def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(email=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('book:home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'login.html')
    
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('book:login'))