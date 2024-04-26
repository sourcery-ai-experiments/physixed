from django.urls import resolve, reverse

from .. import config, views


def test_ui_landing_page() -> None:
    """
    Test the URL mapping for the `ui_landing_page` view.

    This function asserts that the URL resolution for the `ui_landing_page` view matches the expected view function.
    """
    assert resolve(reverse(f"{config.APP_SLUG}:ui_landing_page")).func == views.ui_landing_page
