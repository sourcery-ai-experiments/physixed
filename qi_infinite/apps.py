from django.apps import AppConfig

APP_SLUG = "qi_infinite"


class QiMainConfig(AppConfig):
    """Configure the application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "qi_infinite"
