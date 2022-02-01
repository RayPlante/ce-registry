from django.urls import path

from . import views

app_name = 'editrec'
urlpatterns = [
    path('<str:draft_id>', views.edit, name='edit'),
]
