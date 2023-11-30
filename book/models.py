from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model

Account = get_user_model()


class Author(models.Model):
    name = models.CharField(max_length= 256)
    def __str__(self):
        return f"{self.name}"
    
    
# TODO 紐付け方を考える
class Book(models.Model):
    pub_date = models.DateField("出版日", null=True, blank=True)
    title = models.CharField(max_length=256)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/book', null=True, blank=True)
    favorite_by = models.ManyToManyField(Account, blank=True)
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
    
    class Meta:
        unique_together = ('book','reviewer')
    
    
    

    
    
