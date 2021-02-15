from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'subCategory', 'sum', 'date')


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubcategoryAdmin)
admin.site.register(News, NewsAdmin)
