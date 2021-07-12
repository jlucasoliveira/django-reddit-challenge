from rest_framework import serializers

from helpers.serializers import AuthorCreateMixin, AuthorMixin, NestedObject, TimestampSerializerMixin
from post import models
from topic import models as topic_models


class PostListSerializer(TimestampSerializerMixin):
    author = serializers.StringRelatedField()

    class Meta:
        model = models.Post
        fields = ("pk", "title", "content", "author", "created_at", "updated_at")


class PostSerializer(TimestampSerializerMixin, AuthorCreateMixin):
    topic = serializers.HiddenField(
        default=NestedObject(lookup="topic_url_name", lookup_field="url_name", model=topic_models.Topic)
    )

    class Meta:
        model = models.Post
        fields = ("pk", "title", "content", "author", "topic", "created_at", "updated_at")


class PostRetrieveSerializer(TimestampSerializerMixin, AuthorMixin):
    class Meta:
        model = models.Post
        fields = ("pk", "title", "content", "author", "topic", "created_at", "updated_at")
