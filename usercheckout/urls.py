from django.urls import path
from . import views
from .webhooks import webhook

name = 'usercheckout'

urlpatterns = [
    path('', views.usercheckout, name='usercheckout')
    path('usercheckout_success/<order_number>', views.usercheckout_success, name='usercheckout_success'),
    path('wh/', webhook, name='webhook'),
]