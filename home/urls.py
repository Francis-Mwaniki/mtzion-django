from django.urls import path
from . import views
urlpatterns = [
    path("",views.home, name='home'),
    path("<series>", views.series, name="series"),
    path("<series>/<topic>", views.topic, name="topic"),
   path('nav/<username>/',views.nav,name='nav')
   ]
