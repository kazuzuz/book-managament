from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# カスタムユーザー

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("メールアドレスは必須です")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using= self._db)
        return user        

    
    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        
        return self.create_user(email, password, **kwargs)
    
    
class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50,unique=True, null=True, blank=True)
    email = models.EmailField(max_length=256, unique=True)
    is_staff = models.BooleanField(default=False)
    #追加したいフィールドがある場合はここに追加する

    
    USERNAME_FIELD = "email"
    
    objects = AccountManager()
