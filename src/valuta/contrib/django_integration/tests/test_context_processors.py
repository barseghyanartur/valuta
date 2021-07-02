import os

from django.test import TestCase, override_settings
from django.urls import reverse

from valuta.constants import (
    DEFAULT_DISPLAY_FORMAT,
    DISPLAY_FORMAT_HUMAN_READABLE,
    DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_CODE,
    DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_SYMBOL,
    DISPLAY_FORMAT_NUMBER,
)

from project.settings.core import project_dir

__author__ = "Artur Barseghyan"
__copyright__ = "2021 Artur Barseghyan"
__license__ = "GPL-2.0-only OR LGPL-2.1-or-later"
__all__ = ("ContextProcessorsTestCase",)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [project_dir(os.path.join("..", "templates"))],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "valuta.contrib.django_integration.context_processors.constants",
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "debug": False,
        },
    }
]


class ContextProcessorsTestCase(TestCase):
    """Context processors."""

    @override_settings(TEMPLATES=TEMPLATES)
    def test_context_processors(self):

        response = self.client.get(reverse("home"))
        html = response.rendered_content
        self.assertInHTML(
            f'<p id="DEFAULT_DISPLAY_FORMAT">{DEFAULT_DISPLAY_FORMAT}</p>',
            html,
        )

        self.assertInHTML(
            f'<p id="DISPLAY_FORMAT_HUMAN_READABLE">'
            f"{DISPLAY_FORMAT_HUMAN_READABLE}</p>",
            html,
        )

        self.assertInHTML(
            f'<p id="DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_CODE">'
            f"{DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_CODE}</p>",
            html,
        )

        self.assertInHTML(
            f'<p id="DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_SYMBOL">'
            f"{DISPLAY_FORMAT_HUMAN_READABLE_WITH_CURRENCY_SYMBOL}</p>",
            html,
        )

        self.assertInHTML(
            f'<p id="DISPLAY_FORMAT_NUMBER">{DISPLAY_FORMAT_NUMBER}</p>',
            html,
        )
