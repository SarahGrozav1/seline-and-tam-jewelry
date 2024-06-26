from django.db import models
from profiles.models import UserProfile
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    """A category model for maintaining default
    category information"""
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """A product model for maintaining product
       information"""
    collections = models.ForeignKey('Collections', null=True, blank=True,
                                    on_delete=models.SET_NULL)
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Collections(models.Model):
    """A collections model for maintaining collection
       information"""
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_frienfly_name(self):
        return self.friendly_name


class ReviewRating(models.Model):
    """A review/rating model for maintaining review/rating
       information"""
    user = models.ForeignKey(UserProfile, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    comment = models.TextField(max_length=300)
    rating = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Wishlist(models.Model):
    """A wishlist model for maintaining wishlist
       information"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Wishlist'


class WishlistItem(models.Model):
    """A wishlist item model for maintaining wishlist item
       information of each product added to wishlist"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_at']

    def __str__(self):
        return f'{self.user.username}\'s wishlist item for\
        {self.product.title}'
