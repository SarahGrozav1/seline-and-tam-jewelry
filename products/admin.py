from django.contrib import admin
from.models import Product, Category, Collections

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'collections',
        'category',
        'sku',
        'name',
        'price',
        'image',
        'rating',
    )
    
    ordering = ('sku',)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    
class CollectionsAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Collections, CollectionsAdmin)