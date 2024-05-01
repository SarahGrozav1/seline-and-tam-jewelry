from django.contrib import admin
from .models import Product, Category, Collections, ReviewRating, Wishlist


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'collections',
        'category',
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
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'rating', 'created_on']
    readonly_fields = ['created_on']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Collections, CollectionsAdmin)
admin.site.register(ReviewRating, ReviewAdmin)
admin.site.register(Wishlist)
