from zoneinfo import ZoneInfo

from .apps import APP_SLUG as APP_SLUG_


class Config:
    """Configure the application."""

    APP_SLUG: str = APP_SLUG_
    app_version: str = "0.0.1"
    responsible_person: str = "Leroy Teegelbeckers"
    responsible_person_email: str = "multiduckk@gmail.com"
    browser_tab_name: str = "Main"
    description: str = "Landing portal for all Quantum Insight applications"
    year: str = "2024"
    default_timezone = ZoneInfo("Europe/Amsterdam")


config = Config()
