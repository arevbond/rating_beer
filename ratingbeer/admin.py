from django.contrib import admin

from .models import *


class BeerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_title', 'short_description', 'price', 'alcogol', 'category',
                    'country', 'image', 'time_create', 'is_published')

    list_display_links = ('id', 'short_title')
    list_editable = ('is_published', )
    list_per_page = 15

    ordering = ('id',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = list_display
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Beer, BeerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Country)
