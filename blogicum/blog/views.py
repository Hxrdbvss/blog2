from django.shortcuts import render, get_object_or_404
from .models import Category, Post

def index(request):
    post_list = Post.objects.all()  # Получаем все посты
    return render(request, 'blog/index.html', {'post_list': post_list})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/detail.html', {'post': post})

def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    post_list = Post.objects.filter(category=category)
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_list
    })


