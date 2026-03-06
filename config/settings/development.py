"""Development settings — extends base."""
from .base import *  # noqa: F401, F403
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True

ALLOWED_HOSTS = ["*"]

# MySQL (inherits from base.py via my.cnf — MySQL84 service must be running)
# SQLite fallback: uncomment below and comment out to use SQLite during offline work
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# Windows npm path for django-tailwind
NPM_BIN_PATH = "npm.cmd"

# Hot-reload support
INSTALLED_APPS += ["django_browser_reload"]  # noqa: F405

MIDDLEWARE += [  # noqa: F405
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]
