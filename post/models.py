from __future__ import annotations

from django.db import models
from django.utils.translation import gettext_lazy as _

from helpers.models import AuthorMixin, TimestampModel


class Post(TimestampModel, AuthorMixin):
    topic = models.ForeignKey(
        to="topic.Topic",
        on_delete=models.deletion.CASCADE,
        verbose_name=_("topic"),
        related_name="posts",
        related_query_name="posts",
    )
    title = models.CharField(verbose_name=_("title"), max_length=150)
    content = models.TextField(verbose_name=_("content"))

    class Meta:
        verbose_name = _("post")
        ordering = ("-created_at",)

    def __str__(self: Post) -> str:
        return self.title
