from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Post, Category


def get_formatted_categories_to_menu():
    all_categories = Category.objects.all()

    formatted_categories = list()

    for category in all_categories:
        if not category.parent_category:
            children = Category.objects.filter(parent_category=category)
            formatted_category = {
                'parent': category,
                'children': children
            }
            formatted_categories.append(formatted_category)

    return formatted_categories


# Function Based Views

def index(request):

    formatted_categories = get_formatted_categories_to_menu()

    posts = Post.objects.filter(published=True).order_by('-created_at')
    paginator = Paginator(posts, 10)  # Show 10 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': formatted_categories,
        'posts': posts,
        'page_obj': page_obj
    }

    return render(request, "blog/posts_pagination.html", context)

# DetailView
def posts_details(request, slug):

    formatted_categories = get_formatted_categories_to_menu()

    post = Post.objects.get(slug=slug)

    context = {
        'categories': formatted_categories,
        'post': post,
    }

    return render(request, "blog/post_details.html", context)


def posts_by_category(request, slug):

    formatted_categories = get_formatted_categories_to_menu()

    category = Category.objects.get(slug=slug)
    posts = category.post_set.filter(published=True).order_by('-created_at')
    paginator = Paginator(posts, 10)  # Show 10 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': formatted_categories,
        'posts': posts,
        'page_obj': page_obj,
    }

    return render(request, "blog/posts_pagination.html", context)



# Class Based Views

# from django.views.generic import ListView

# class PostListView(ListView):
#     template_name = "blog/posts_pagination.html"
#     model = Post
#     context_object_name = "posts" # default: "object"

# class PostUpdateView(UpdateView):
#     template_name = 'atualiza.html'
#     model = Funcionario
#     fields = [
#         'nome',
#         'sobrenome',
#         'cpf',
#         'tempo_de_servico',
#         'remuneracao'
#     ] # fields = '__all__'


# TemplateView: para renderizar uma página (apenas uma página simples)

# ListView: listar todos os objetos
# CreateView : Para criar de objetos (É o Create do CRUD)
# DetailView : Traz os detalhes de um objeto (É o Retrieve do CRUD)
# UpdateView : Para atualização de um objeto (É o Update do CRUD)
# DeleteView : Para deletar objetos (É o Delete do CRUD)

