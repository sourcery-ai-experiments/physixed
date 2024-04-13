import pytest
from django.test import RequestFactory
from django.urls import reverse
import numpy as np
from ..views import ui_landing_page

from .. import config


def test_ui_landing_page():
    factory = RequestFactory()
    request = factory.get(reverse(config.APP_SLUG + ":ui_landing_page"))

    response = ui_landing_page(request)

    assert response.status_code == 200
