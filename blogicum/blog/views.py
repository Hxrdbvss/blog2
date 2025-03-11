from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.filter(is_published=True).order_by('-pub_date')
    reversed_posts = posts[:5]  # Например, берём последние 5 постов
    context = {'posts': reversed_posts}
    return render(request, 'blog/index.html', context)

def post_detail(request, id):
    """Страница отдельного поста."""
    post = next((p for p in posts if p["id"] == id), None)
    context = {"post": post}
    if not post:
        return render(request, '404.html', status=404)  # Если пост не найден
    return render(request, 'blog/detail.html', context)
    #return render(request, "blog/detail.html", context)

def category_posts(request, category_slug):
    """Посты определенной категории."""
    filtered_posts = [p for p in posts if p["category"] == category_slug]
    context = {"posts": filtered_posts, "category": category_slug}
    return render(request, "blog/category.html", context)


