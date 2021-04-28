from django.urls import path

from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<str:slug>/', views.posts_details, name='posts_details'),
    path('category/<str:slug>/posts', views.posts_by_category, name='posts_by_category'),
]
