from __future__ import annotations

from typing import Any

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from helpers.models import AuthorMixin, TimestampModel


class Topic(TimestampModel, AuthorMixin):
    name = models.CharField(verbose_name=_("name"), max_length=50)
    url_name = models.SlugField(verbose_name=_("URL name"), db_index=True)
    title = models.CharField(verbose_name=_("title"), max_length=150)
    description = models.TextField(
        verbose_name=_("description"),
        max_length=350,
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

    @property
    def latests_posts(self: Topic) -> models.QuerySet:
        return self.posts.all()[:15]


class Post(TimestampModel, AuthorMixin):
    topic = models.ForeignKey(
        to="posts.Topic",
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


class Comment(TimestampModel, AuthorMixin):
    post = models.ForeignKey(
        to="posts.Post",
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
