from django.apps import AppConfig

APP_SLUG = "px_kinematics"


class PxKinematicsConfig(AppConfig):
    """
    Configure the `px_kinematics` app.

    This class sets the default auto field to "django.db.models.BigAutoField" for the `px_kinematics` app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "px_kinematics"
