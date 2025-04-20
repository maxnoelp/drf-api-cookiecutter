import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "portfolio_api_v1.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import portfolio_api_v1.users.signals  # noqa: F401
