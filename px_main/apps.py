from django.apps import AppConfig

APP_SLUG = "px_main"


class QiMainConfig(AppConfig):
    """Configure the application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "px_main"
