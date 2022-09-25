from django.db import models
from django.urls import reverse
from django.template.defaultfilters import truncatechars


class Beer(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    alcogol = models.FloatField(default=5, verbose_name='Алкоголь')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True,
                                 verbose_name='Категория')
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True,
                                verbose_name='Страна')
    image = models.ImageField(upload_to='media/%Y/%m/%d', height_field=200, width_field=200,
                              verbose_name='Фото')
    slug = models.SlugField(verbose_name='Slug')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    @property
    def short_title(self):
        return truncatechars(self.title, 20)
    @property
    def short_description(self):
        return truncatechars(self.description, 35)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пиво'
        verbose_name_plural = 'Пиво'
        ordering = ['id']


class Country(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страна'
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Категория')
    desc = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']
