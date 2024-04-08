from django.urls import path
from . import views

name = 'usercheckout'

urlpatterns = [
    path('', views.usercheckout, name='usercheckout')
]