from django.urls import path

from . import views

app_name = 'createrec'
urlpatterns = [
    path('', views.index, name='index'),
    path('start', views.start, name='start'),
]
