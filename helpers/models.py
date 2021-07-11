from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampModel(models.Model):
    """
    Extend this model if you wish to have automatically updated
    created_at and updated_at fields.
    """

    class Meta:
        abstract = True

    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)


class AuthorMixin(models.Model):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.deletion.SET_NULL,
        null=True,
        verbose_name=_("author"),
    )

    class Meta:
        abstract = True
