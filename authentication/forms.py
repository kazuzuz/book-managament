from django import forms
from django.contrib.auth.forms import UserCreationForm

from authentication.models import Account

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")
    
    class Meta:
        model = Account
        fields = [ 'email', 'password']

    