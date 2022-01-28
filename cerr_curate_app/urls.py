from django.urls import re_path
from cerr_curate_app.views.user import views as user_cerr_views, ajax as ajax

urlpatterns = [
    re_path(r"^$", user_cerr_views.get_name, name="core_curate_index"),

]