from django.apps import AppConfig

APP_SLUG = "qi_main"


class QiMainConfig(AppConfig):
    """Configure the application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "qi_main"
