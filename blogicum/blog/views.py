from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Category, Post

def index(request):
    # Главная страница: 5 последних публикаций
    post_list = Post.objects.filter(
        is_published=True,                  # Публикация опубликована
        pub_date__lte=timezone.now(),       # Дата публикации не позже текущего времени
        # Учитываем, что category может быть null
        models.Q(category__is_published=True) | models.Q(category__isnull=True)
    ).order_by('-pub_date')[:5]             # Сортировка по убыванию даты, первые 5
    return render(request, 'blog/index.html', {'post_list': post_list})

def post_detail(request, id):
    # Страница отдельной публикации
    post = get_object_or_404(Post.objects.filter(
        is_published=True,                  # Публикация опубликована
        pub_date__lte=timezone.now(),       # Дата публикации не позже текущего времени
        # Учитываем, что category может быть null
        models.Q(category__is_published=True) | models.Q(category__isnull=True)
    ), id=id)
    return render(request, 'blog/detail.html', {'post': post})

def category_posts(request, category_slug):
    # Страница категории: только посты с конкретной категорией
    category = get_object_or_404(Category, slug=category_slug, is_published=True)
    post_list = Post.objects.filter(
        category=category,                  # Принадлежит выбранной категории
        is_published=True,                  # Публикация опубликована
        pub_date__lte=timezone.now()        # Дата публикации не позже текущего времени
    ).order_by('-pub_date')
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_list
    })