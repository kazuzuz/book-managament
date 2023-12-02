from django.contrib import admin

from book.models import Book, Review, Author, Tag
from authentication.models import Account
# Register your models here.
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Account)
admin.site.register(Author)
admin.site.register(Tag)