from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_id>/', views.posts_details, name='posts_details'),
    path('category/<int:category_id>/posts/', views.posts_by_category, name='posts_by_category'),
    # path('category/<slug>/posts', views.category_posts, name='category_posts'),
]
