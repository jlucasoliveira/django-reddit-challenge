from __future__ import annotations

from typing import Optional, Type

from rest_framework import serializers
from rest_framework.exceptions import NotFound

from django.db.models import Model
from django.utils.translation import gettext_lazy as _


class NestedObject:
    requires_context = True

    def __init__(
        self: NestedObject,
        *,
        lookup: str,
        lookup_field: Optional[str] = None,
        model: Type[Model],
    ) -> None:
        self.model = model

        self.lookup = lookup
        if not lookup_field:
            lookup_field = lookup
        self.lookup_field = lookup_field

    def __call__(self: NestedObject, serializer_field: serializers.Field) -> int:
        try:
            _id = serializer_field.context["kwargs"].get(self.lookup)
            obj = self.model.objects.get(**{self.lookup_field: _id})
        except self.model.DoesNotExist:
            raise NotFound(_("%s has not found for passed field" % self.model.__name__))
        return obj

    def __repr__(self: NestedObject) -> str:
        return f"{self.__class__.__name__}()"


class TimestampSerializerMixin(serializers.ModelSerializer):
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)


class AuthorCreateMixin(serializers.Serializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
