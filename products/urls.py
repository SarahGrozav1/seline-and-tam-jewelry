
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.detail_product, name='detail_product'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),

]
