
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.detail_product, name='detail_product'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
    path('editreview/<int:product_id>/<int:review_id>/', views.edit_review, name='edit_review'),
    path('deletereview/<int:product_id>/<int:review_id>/', views.delete_review, name='delete_review'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('remove_from_wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
