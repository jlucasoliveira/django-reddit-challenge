from __future__ import annotations

from typing import Any

from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from helpers.models import TimestampModel


class Topic(TimestampModel):
    name = models.CharField(verbose_name=_("name"), max_length=50)
    url_name = models.SlugField(verbose_name=_("URL name"), db_index=True)
    title = models.CharField(verbose_name=_("title"), max_length=150)
    description = models.TextField(
        verbose_name=_("description"),
        max_length=350,
    )
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.deletion.SET_NULL,
        null=True,
        verbose_name=_("author"),
    )

    class Meta:
        verbose_name = _("topic")
        ordering = ("-created_at",)

    def __init__(self: Topic, *args: Any, **kwargs: Any) -> None:
        super(Topic, self).__init__(*args, **kwargs)
        self._name = self.name

    def save(self: Topic, *args: Any, **kwargs: Any) -> None:
        if not self.url_name or self._name != self.name:
            self.url_name = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self: Topic) -> str:
        return self.title
