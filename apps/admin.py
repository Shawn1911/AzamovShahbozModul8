from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Category, Product


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass
