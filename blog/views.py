from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Post, Category


def index(request):

    categories = Category.objects.all()

    posts = Post.objects.filter(published=True).order_by('-created_at')
    paginator = Paginator(posts, 10)  # Show 10 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'posts': posts,
        'page_obj': page_obj
    }

    return render(request, "blog/index.html", context)


def posts_details(request, post_id):

    categories = Category.objects.all()

    post = Post.objects.get(id=post_id)

    context = {
        'categories': categories,
        'post': post,
    }

    return render(request, "blog/post_details.html", context)


def posts_by_category(request, category_id):

    categories = Category.objects.all()

    category = Category.objects.get(id=category_id)
    posts = category.post_set.filter(published=True).order_by('-created_at')

    context = {
        'categories': categories,
        'posts': posts,
        'category': category
    }

    return render(request, "blog/posts_by_category.html", context)
