from django.urls import path

from . import views

app_name = 'createrec'
urlpatterns = [
    path('', views.start, name='index'),
    path('start', views.start, name='start'),
]
