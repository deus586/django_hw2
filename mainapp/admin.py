from django.contrib import admin

from mainapp.models import Product, Category
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
