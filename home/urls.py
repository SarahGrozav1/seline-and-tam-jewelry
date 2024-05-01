from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
    path('contact_form', views.contact_form, name='contact_form' ),  
]
