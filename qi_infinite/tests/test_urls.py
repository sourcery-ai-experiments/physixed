import pytest

from django.urls import reverse, resolve
from .. import config
from .. import views

def test_ui_landing():

    assert resolve(reverse(f"{config.APP_SLUG}:ui_landing_page")).func == views.ui_landing_page
