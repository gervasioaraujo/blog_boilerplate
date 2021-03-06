from django.contrib import admin

from .models import Category, Post
from .forms import PostModelForm


class CategoryModelAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'slug',
        'parent_category',
    )

    fields = ('name', 'parent_category',)


class PostModelAdmin(admin.ModelAdmin):

    list_display = (
        # 'id',
        'title',
        # 'categories',
        'author',
        'slug',
        'published',
        'created_at',
        'updated_at',
    )

    form = PostModelForm

    fields = ('title', 'categories', 'thumbnail', 'content',
              'summary', 'published', 'created_at', 'updated_at')

    readonly_fields = ('created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super(PostModelAdmin, self).save_model(request, obj, form, change)


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Post, PostModelAdmin)
