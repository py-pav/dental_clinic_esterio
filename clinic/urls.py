from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('doctors/', views.doctors, name='doctors'),
    path('promotions/', views.promotions, name='promotions'),
    path('reviews/', views.reviews, name='reviews'),
    path('contacts/', views.contacts, name='contacts'),
]
