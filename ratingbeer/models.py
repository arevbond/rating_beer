from django.db import models
from django.urls import reverse
from django.template.defaultfilters import truncatechars
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import CheckConstraint, Q, UniqueConstraint


class Beer(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена', null=True, blank=True)
    alcogol = models.FloatField(default=5, verbose_name='Алкоголь')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True,
                                 verbose_name='Категория')
    country = models.CharField(null=True, verbose_name='Страна', max_length=255)
    image = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Фото', blank=True)
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    @property
    def short_title(self):
        new_name = ''
        for word in self.title.split():
            if word[0].isupper():
                new_name += word + ' '
        if new_name.split()[0] == 'Пивной':
            new_name = new_name.split()
            new_name[0] = 'Пивной напиток'
            new_name = ' '.join(new_name)
        return new_name

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


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class Rating(models.Model):
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, verbose_name='Пиво')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            CheckConstraint(check=Q(rate__range=(0, 10)), name='valid_rate'),
        ]
        # UniqueConstraint(fields=['user', 'beer'], name='rating_once')


class Comment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True, blank=True, null=True)
    update = models.DateField(auto_now=True, blank=True, null=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('add_comment', kwargs={'post_id': self.beer.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to='images/profile/', blank=True,)
    rang = models.ForeignKey('Rang', on_delete=models.CASCADE, null=True, blank=True)



class Rang(models.Model):
    title = models.CharField(max_length=200, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title