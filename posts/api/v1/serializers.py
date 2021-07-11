from rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

from helpers.serializers import AuthorCreateMixin, NestedObject, TimestampSerializerMixin
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
    topic = serializers.HiddenField(
        default=NestedObject(
            lookup="topic_url_name",
            lookup_field="url_name",
            model=models.Topic,
        )
    )

    class Meta:
        model = models.Post
        fields = ("pk", "title", "content", "author", "topic", "created_at", "updated_at")


class CommentSerializer(TimestampSerializerMixin, AuthorCreateMixin):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = serializers.HiddenField(
        default=NestedObject(
            lookup="post_pk",
            lookup_field="pk",
            model=models.Post,
        )
    )

    class Meta:
        model = models.Comment
        fields = ("pk", "title", "content", "author", "post", "created_at", "updated_at")
