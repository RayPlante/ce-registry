"""cerr_curate_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin

from .views.user import draft
from .views.user import ajax

app_name = "draft"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("draft/start/", draft.start, name="start"),
    path("draft/edit/<str:draft_id>", draft.EditView.as_view(), name="edit"),
    path(
        r"^save-list-data", ajax.data_structure_element_value, name="ajax_save_element"
    ),
]
