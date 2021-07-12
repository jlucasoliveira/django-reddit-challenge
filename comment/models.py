from __future__ import annotations

from django.db import models
from django.utils.translation import gettext_lazy as _

from helpers.models import AuthorMixin, TimestampModel


class Comment(TimestampModel, AuthorMixin):
    post = models.ForeignKey(
        to="post.Post",
        on_delete=models.deletion.CASCADE,
        verbose_name=_("post"),
        related_name="comments",
        related_query_name="comments",
    )
    title = models.CharField(
        verbose_name=_("title"),
        max_length=250,
    )
    content = models.TextField(
        verbose_name=_("content"),
        max_length=350,
    )

    class Meta:
        verbose_name = _("comment")
        ordering = ("-updated_at",)

    def __str__(self: Comment) -> str:
        return self.title
