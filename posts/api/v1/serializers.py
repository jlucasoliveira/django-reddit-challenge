from rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

from helpers.serializers import AuthorCreateMixin, TimestampSerializerMixin
from posts import models


class TopicListSerializer(TimestampSerializerMixin):
    author = UserDetailsSerializer(read_only=True)

    class Meta:
        model = models.Topic
        fields = ("pk", "name", "title", "url_name", "author", "description", "created_at", "updated_at")


class TopicSerializer(TimestampSerializerMixin, AuthorCreateMixin):
    url_name = serializers.SlugField(read_only=True)

    class Meta:
        model = models.Topic
        fields = ("name", "title", "url_name", "author", "description", "created_at", "updated_at")


class PostListSerializer(TimestampSerializerMixin, AuthorCreateMixin):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Post
        fields = ("pk", "title", "content", "author", "topic", "created_at", "updated_at")
