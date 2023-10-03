from django.contrib import admin

from book.models import Book, Review
from authentication.models import Account
# Register your models here.
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Account)