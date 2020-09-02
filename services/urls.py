from django.urls import path 
from . import views


urlpatterns = [
    path('services/', views.services, name='services'),
    path('services/about', views.about, name='about'),
    path('services/our_brands', views.our_brands, name='our_brands'),
    path('services/contact_us', views.about, name='contact_us'),
  ]


