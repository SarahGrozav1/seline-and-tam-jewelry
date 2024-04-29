from django.contrib import admin
from products.models import ReviewRating

# Register your models here.

@admin.register(ReviewRating)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'rating', 'created_on']
    readonly_fields = ['created_on']
