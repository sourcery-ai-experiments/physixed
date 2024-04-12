from django.urls import resolve, reverse

from .. import config, views


def test_entry_point():

    assert resolve(reverse(f"{config.APP_SLUG}:ui_landing_page")).func == views.ui_landing_page
