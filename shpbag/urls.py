from django.urls import path
from . import views

app_name = 'shpbag'

urlpatterns = [
    path('', views.shp_bag, name='shp_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    
]
