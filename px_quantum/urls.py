from django.urls import path

from . import config, views

app_name = config.APP_SLUG

urlpatterns = [
   path("", views.ui_landing_page, name="ui_landing_page"),
]
