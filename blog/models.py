from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):

    name = models.CharField(max_length=100, unique=True, verbose_name='nome')
    slug = models.SlugField(max_length=150, null=True, unique=True)
    parent_category = models.ForeignKey('self', blank=True, null=True,
                                        verbose_name='categoria pai', on_delete=models.SET_NULL)

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
    summary = models.CharField(
        max_length=300, null=True, blank=True, verbose_name='resumo')
    categories = models.ManyToManyField(Category, verbose_name='categorias')
    # category = models.ForeignKey(Category, blank=False, null=True,
    #                              verbose_name='categoria', on_delete=models.SET_NULL)
    author = models.ForeignKey(
        User, null=True, verbose_name='autor', on_delete=models.SET_NULL)
    thumbnail = models.ImageField(
        upload_to='uploads', verbose_name='imagem destacada', blank=True, null=True)

    slug = models.SlugField(max_length=300, null=True, unique=True)

    # STATUS_OPTIONS = (
    #     ('private', 'Privado'),
    #     ('published', 'Publicado'),
    # )
    published = models.BooleanField(default=False, verbose_name='publicado')

    created_at = models.DateTimeField(
        null=True, verbose_name='criado em', auto_now_add=True)
    updated_at = models.DateTimeField(
        null=True, verbose_name='atualizado em', auto_now=True)

    def save(self, *args, **kwargs):

        slug = slugify(self.title)

        post_with_same_slug = Post.objects.filter(slug__iexact=slug).first()

        if post_with_same_slug and not post_with_same_slug.id == self.id:
            self.slug = f"{slug}-id-{self.id}"

        if not post_with_same_slug:
            self.slug = slug

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# https://learndjango.com/tutorials/django-slug-tutorial
