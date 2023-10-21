from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ABOUT-US', views.about_us, name='ABOUT-US'),
    path('OUR-SERVICES', views.our_services, name='OUR-SERVICES'),
]
