from django.urls import path
from . import views

app_name = 'shpbag'

urlpatterns = [
    path('', views.shp_bag, name='shp_bag'),
    
]
