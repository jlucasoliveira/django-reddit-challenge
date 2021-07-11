from __future__ import annotations

from rest_framework import serializers


class TimestampSerializerMixin(serializers.ModelSerializer):
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)


class AuthorCreateMixin(serializers.Serializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
