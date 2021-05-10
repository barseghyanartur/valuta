from django.conf.urls import re_path
from django.contrib import admin
from django.views.generic import TemplateView

__all__ = ("urlpatterns",)

urlpatterns = [
    re_path(
        "^$", view=TemplateView.as_view(template_name="home.html"), name="home"
    ),
    re_path(r"^admin/", admin.site.urls),
]
