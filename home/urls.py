from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
#    path( '', views.home/about, 'home/about', name='about')
]

