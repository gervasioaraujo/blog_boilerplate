from django.contrib import admin

from .models import Category, Post


class CategoryModelAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'slug',
        'parent_category',
    )

    fields = ('name', 'parent_category',)


class PostModelAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        # 'categories',
        'author',
        'slug',
        'published',
        'created_at',
        'updated_at',
    )

    fields = ('title', 'categories', 'thumbnail', 'content', 'published')

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super(PostModelAdmin, self).save_model(request, obj, form, change)


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Post, PostModelAdmin)
