from django.db import models
from django.utils import timezone
import datetime

from django.contrib.auth import get_user_model

Account = get_user_model()

class Book(models.Model):
    pub_date = models.DateField("出版日", null=True, blank=True)
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    
    def __str__(self):
        return f"[{self.author}] {self.title}"
    
        

class Review(models.Model):
    created_at = models.DateTimeField("レビュー日", default=timezone.now)
    book = models.ForeignKey(Book, on_delete=models.CASCADE) 
    review_text = models.CharField(max_length=256, blank=True)
    score = models.IntegerField(default=0)
    
    reviewer = models.ForeignKey(
        Account, on_delete=models.CASCADE, null=True, blank=True
    )
    def __str__(self):
        return f"「{self.book.title}」のレビュー"