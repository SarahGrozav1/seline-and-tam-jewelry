from django.db import models

# Create your models here.

class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name

    def get_frienfly_name(self):
        return self.friendly_name
    
class Product(models.Model):
    collections = models.ForeignKey('Collections', null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Collections(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name

    def get_frienfly_name(self):
        return self.friendly_name