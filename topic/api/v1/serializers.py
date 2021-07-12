from rest_framework import serializers

from helpers.serializers import AuthorCreateMixin, AuthorMixin, TimestampSerializerMixin
from post.api.v1 import serializers as post_serializers
from topic import models


class TopicListSerializer(TimestampSerializerMixin):
    author = serializers.StringRelatedField()

    class Meta:
        model = models.Topic
        fields = ("pk", "name", "title", "url_name", "author", "created_at", "updated_at")


class TopicRetrieveSerializer(TimestampSerializerMixin, AuthorMixin):
    posts = post_serializers.PostListSerializer(many=True, source="latests_posts")

    class Meta:
        model = models.Topic
        fields = ("pk", "name", "title", "url_name", "author", "description", "posts", "created_at", "updated_at")


class TopicSerializer(TimestampSerializerMixin, AuthorCreateMixin):
    url_name = serializers.SlugField(read_only=True)

    class Meta:
        model = models.Topic
        fields = ("name", "title", "url_name", "author", "description", "created_at", "updated_at")
