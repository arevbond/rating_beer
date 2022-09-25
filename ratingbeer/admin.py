from django.contrib import admin

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class BeerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_title', 'short_description', 'price', 'alcogol', 'category', 'country',
                    'image', 'time_create', 'is_published')

    list_display_links = ('id', 'short_title')
    list_editable = ('is_published', )



class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Beer, BeerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Country)
