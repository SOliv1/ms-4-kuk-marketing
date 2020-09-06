from django.urls import path
from . import views


urlpatterns = [

    path('services/about', views.about, name='about'),
    path('services/our_brands', views.our_brands, name='our_brands'),
    path('services/contact_us', views.contact_us, name='contact_us'),
    path('services/our_services', views.our_services, name='our_services'),
    path('services/brands', views.brands, name='brands'),
    path('services/contact', views.contact, name='contact'),
    path('services/graphic_design',
         views.graphic_design, name='graphic_design'),
    path('services/web_design',
         views.web_design, name='web_design'),
    path('services/web_devlepment',
         views.web_development, name='web_development'),
    path('services/digital_marketing',
         views.digital_marketing, name='digital_marketing'),
]