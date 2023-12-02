from django.shortcuts import render
from book.models import  Book, Author, Tag
from django.core.paginator import Paginator
# Create your views here.

def search(request):
    search_word = request.GET.get('search_word')
    
    if not search_word:
        context ={
            'search_word': "",
            'books' : [],
        }
        return render(request, "search_result.html", context)
    
    books = Book.objects.filter(title__icontains=search_word)
    
    #pagenation
    limit = 1
    paginator = Paginator(books, limit)
    page_number = request.GET.get('page', 1)
    result = paginator.get_page(page_number)
    pages_num_list = list(paginator.page_range)
    
    context = {
        'search_word': search_word, 'books': result, 'pages_num_list': pages_num_list   
    }
    
    return render(request, "search_result.html", context)

def author_search(request):
    search_word = request.GET.get('search_word')
    
    if not search_word:
        context ={
            'search_word': "",
            'books' : [],
        }
        return render(request, "author_search_result.html", context)
    
    author = Author.objects.filter(name__icontains=search_word)
    books = Book.objects.filter(author__in=author)
    
    #pagenation
    limit = 1
    paginator = Paginator(books, limit)
    page_number = request.GET.get('page', 1)
    result = paginator.get_page(page_number)
    pages_num_list = list(paginator.page_range)
    
    context = {
        'search_word': search_word, 'books': result, 'pages_num_list': pages_num_list   
    }
    
    return render(request, "author_search_result.html", context)    

def tag_search(request):
    input_tag = request.GET.get('tag_name')
    tag = Tag.objects.get(name__iexact=input_tag)
    books = Book.objects.filter(tag__in=[tag])
    
    #pagenation
    limit = 1
    paginator = Paginator(books, limit)
    page_number = request.GET.get('page', 1)
    result = paginator.get_page(page_number)
    pages_num_list = list(paginator.page_range)
    
    context = {
        'tag_name': tag, 'books': result, 'pages_num_list': pages_num_list   
    }
    
    return render(request, "tag_search_result.html", context)
    

    
    