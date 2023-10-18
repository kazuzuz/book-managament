from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from authentication.models import Account
from django.contrib.auth import authenticate, login, logout
from .models import Account
from .forms import RegisterForm


#登録ページからの情報を受け取り、保存する関数
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return HttpResponseRedirect(reverse("book:home"))
        else:
            print(form.errors)
    form = RegisterForm()
    
    return render(request, "register.html", {"form":form})        

#ログイン処理を行う関数
def login_page(request):
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
                return HttpResponseRedirect(reverse('book:dashboard'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'login.html')

#ログアウトするための関数    

def logout_page(request):
    logout(request)

    return render(request, template_name="logout.html")
