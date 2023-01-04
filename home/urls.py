from django.urls import path
from . import views
urlpatterns = [
   path("",views.home, name='home'),
   path("<series>", views.series, name="series"),
   path("<series>/<topic>", views.topic, name="topic"),
   path('nav/<username>/',views.nav,name='nav'),
   path("new_series/", views.new_series, name="series-create"),
   path("new_post/", views.new_post, name="post-create"),
   path("<series>/update/", views.series_update, name="series_update"),
   path("<series>/delete/", views.series_delete, name="series_delete"),
   path("<series>/<topic>/update/", views.topic_update, name="topic_update"),
   path('<series>/<topic>/update/upload_image/', views.upload_image, name="upload_image"),
   path("<series>/<topic>/delete/", views.topic_delete, name="topic_delete"),
   ]
