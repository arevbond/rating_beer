from django.db import models


class Country(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.title


class Beer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    alcogol = models.FloatField(default=5)
    # category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # country = models.ForeignKey(Country, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='media/%Y/%m/%d', height_field=200, width_field=200)
    slug = models.SlugField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
