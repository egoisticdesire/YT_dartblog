from django.db import models
from django.urls import reverse

'''
    Category:
        title,
        slag
    Tag:
        title,
        slug
    Post:
        title,
        slug,
        author,
        content,
        created_at,
        photo,
        views,
        category,
        tags
'''


class Category(models.Model):
    title = models.CharField(
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name='URL',
        max_length=255,
        unique=True,
    )

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name='URL',
        max_length=50,
        unique=True,
    )

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name='URL',
        max_length=255,
        unique=True,
    )
    author = models.CharField(
        max_length=100,
    )
    content = models.TextField(
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name='Published',
        auto_now_add=True,
    )
    photo = models.ImageField(
        upload_to='photo/%Y/%m/%d/',
        blank=True,
    )
    views = models.IntegerField(
        default=0,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='posts',
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='posts',
    )

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']
