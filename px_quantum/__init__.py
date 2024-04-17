"""Quantum Mechanics package."""

from zoneinfo import ZoneInfo

from .apps import APP_SLUG as APP_SLUG_


class Config:
    """Configure the application."""

    APP_SLUG: str = APP_SLUG_
    app_tile: str = "Infinite well"
    app_version: str = "0.0.1"
    responsible_person: str = "Leroy Teegelbeckers"
    responsible_person_email: str = "multiduckk@gmail.com"
    browser_tab_name: str = "Infinite"
    description: str = "Calculate eigenfunctions of infinite square well"
    year: str = "2024"
    default_timezone = ZoneInfo("Europe/Amsterdam")


config = Config()
