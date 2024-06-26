from django.urls import path
from . import views
from .webhooks import webhook

name = 'usercheckout'

urlpatterns = [
    path('', views.usercheckout, name='usercheckout'),
    path('usercheckout_success/<order_number>', views.usercheckout_success, name='usercheckout_success'),
    path('cache_checkout_data/', views.cache_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]