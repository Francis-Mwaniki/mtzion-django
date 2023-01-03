from . import views
from django.urls import path

urlpatterns = [
    path('register/',views.register, name='register'),
    path('login', views.custom_login, name='login'),
    path('logout', views.custom_logout, name='logout'),
]
