from django.db import models
from django.utils import timezone
import datetime

class Book(models.Model):
    pub_date = models.DateTimeField("date published", default=timezone.now)
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    
        

class Review(models.Model):
    pub_date = models.DateTimeField("date published", default=timezone.now)
    book = models.ForeignKey(Book, on_delete=models.CASCADE) 
    review_text = models.CharField(max_length=256, blank=True)
    score = models.IntegerField(default=0)
