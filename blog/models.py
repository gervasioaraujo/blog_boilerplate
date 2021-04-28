from django.db import models
from django import forms
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError


class Category(models.Model):

    name = models.CharField(max_length=100, unique=True, verbose_name='nome')
    slug = models.SlugField(max_length=150, unique=True)
    parent_category = models.ForeignKey('self', blank=True, null=True,
                                        verbose_name='categoria pai', on_delete=models.SET_NULL)

    def clean(self):
        if self.parent_category and self.parent_category.parent_category:
            raise forms.ValidationError(
                u'A categoria pai escolhida já tem uma categoria pai associada a ela!')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = "categorias"


class Post(models.Model):

    title = models.CharField(max_length=255, verbose_name='título')
    content = RichTextUploadingField(verbose_name='conteúdo')
    # summary = RichTextField(max_length=300, verbose_name='resumo')
    summary = models.CharField(max_length=300, verbose_name='resumo')

    categories = models.ManyToManyField(Category, verbose_name='categorias')
    author = models.ForeignKey(
        User, null=True, verbose_name='autor', on_delete=models.SET_NULL)
    thumbnail = models.ImageField(
        upload_to='uploads', verbose_name='imagem destacada', blank=True, null=True)
    slug = models.SlugField(max_length=300, unique=True)
    published = models.BooleanField(default=False, verbose_name='publicado')
    created_at = models.DateTimeField(
        null=True, verbose_name='criado em', auto_now_add=True)
    updated_at = models.DateTimeField(
        null=True, verbose_name='atualizado em', auto_now=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = Post.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = Post.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# https://learndjango.com/tutorials/django-slug-tutorial


class Comment(models.Model):

    post = models.ForeignKey(
        Post, verbose_name='post', on_delete=models.CASCADE)
    email = models.CharField(max_length=50, verbose_name='email')
    # email = models.ForeignKey(Email, verbose_name='email', on_delete=models.CASCADE)
    content = models.TextField(max_length=255, verbose_name='conteúdo')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'comentário'
        verbose_name_plural = "comentários"


# class CommentReply(models.Model):

#     comment = models.ForeignKey(
#         Comment, verbose_name='comentário', on_delete=models.CASCADE)
#     content = models.TextField(max_length=255, verbose_name='conteúdo')

#     def __str__(self):
#         return self.content
