from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from authentication.models import Account
from django.contrib.auth import authenticate, login, logout
from .models import Account
from .forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView


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
# def login_page(request):
#     form = LoginForm
#     return render(request, 'login.html', {"form":form})

class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    

#ログアウトするための関数    

def logout_page(request):
    logout(request)

    return render(request, template_name="logout.html")
