from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.passenger_login, name='passenger_login'),
    path('details/', views.passenger_dashboard, name='passenger_dashboard'),
    path('success/', views.passenger_success, name='passenger_success'),
]