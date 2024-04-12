from django.urls import resolve, reverse

from .. import config, views


def test_ui_landing():

    assert resolve(reverse(f"{config.APP_SLUG}:ui_landing_page")).func == views.ui_landing_page
