from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator
import re
# articles/views.py

def article_list(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')

    video_pattern = re.compile(r'(youtube\.com|vimeo\.com|iframe)', re.IGNORECASE)
    articles = Article.objects.exclude(description__iregex=video_pattern.pattern).order_by('-pub_date')

    if query:
        articles = articles.filter(title__icontains=query)

    if isinstance(category, str) and category.strip():
        articles = articles.filter(category__iexact=category.strip())

    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = ['Technology', 'Science', 'Business', 'Health', 'Education']

    return render(request, 'articles/article_list.html', {
        'page_obj': page_obj,
        'query': query,
        'category': category,
        'categories': categories,
    })





def home(request):
    query = request.GET.get('q', '')
    articles = Article.objects.filter(title__icontains=query) if query else Article.objects.all()
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'articles/home.html', {'page_obj': page_obj, 'query': query})

def categories(request):
    return render(request, 'articles/categories.html')

def about(request):
    return render(request, 'articles/about.html')

def contact(request):
    return render(request, 'articles/contact.html')
