from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from dotenv import dotenv_values

try:
    from .qi_production_apps import baseline_apps, production_apps
except ImportError:
    assert False, "CRITICAL: Can't import `datamore_production_apps.py`"

try:
    if settings.DEBUG or settings.DJANGO_UNITTESTING:
        from .qi_development_apps import development_apps
except ImportError:
    print("Can't import `qi_development_apps.py`. Using the production_app dict instead.")
    development_apps = production_apps.copy()


oauthsettings = {k.replace("oauth__", ""): v for k, v in dotenv_values(dotenv_path=".env").items()}


urlpatterns = [
    path("admin/", admin.site.urls),
]

# Django debug toolbar:
if settings.DEBUG:
    urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)


def update_urlpatterns(mount_point: str, app_directory: str, urlpatterns: list) -> None:
    """Return a path object to add the 'urlpatterns'.

    Args:
        mount_point (str): mounting point of the app in the root of the project
        app_directory (str): name of the directory in the Quantum Insight project
        urlpatterns (list): list of urls

    """

    directory_base = app_directory.split(".")[0]
    if mount_point is not None:
        if mount_point.startswith("/"):
            mount_point = mount_point[1:]
        if not (mount_point.endswith("/")) and len(mount_point) > 0:
            mount_point += "/"
        urlpatterns.append(
            path(
                mount_point,
                include(
                    f"{directory_base!s}.urls",
                ),
            )
        )


for app_directory, val in baseline_apps.items():
    update_urlpatterns(str(val["mount_point"]), app_directory, urlpatterns)

if settings.DEBUG or settings.DJANGO_UNITTESTING:
    # We are on development/debug mode, or we are running unit tests.
    for app_directory, val in development_apps.items():
        update_urlpatterns(str(val["mount_point"]), app_directory, urlpatterns)

else:
    # We are on production!
    for app_directory, val in production_apps.items():
        update_urlpatterns(str(val["mount_point"]), app_directory, urlpatterns)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
