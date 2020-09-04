from django.urls import path
from . import views


urlpatterns = [
    path('/about/', views.about, name='about'),
    path('/our_brands/', views.our_brands, name='our_brands'),
    path('/contact_us/', views.about, name='contact_us.html'),
]
