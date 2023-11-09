from django import forms
from django.contrib.auth.forms import AuthenticationForm

from authentication.models import Account

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")
    
    class Meta:
        model = Account
        fields = [ 'username','email', 'password']
        
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

    