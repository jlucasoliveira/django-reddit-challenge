from rest_framework import serializers

from helpers.serializers import AuthorCreateMixin, AuthorMixin, NestedObject, TimestampSerializerMixin
from posts import models


class PostListSerializer(TimestampSerializerMixin):
    author = serializers.StringRelatedField()

    class Meta:
        model = models.Post
        fields = ("pk", "title", "content", "author", "created_at", "updated_at")


class TopicListSerializer(TimestampSerializerMixin):
    author = serializers.StringRelatedField()

    class Meta:
        model = models.Topic
        fields = ("pk", "name", "title", "url_name", "author", "created_at", "updated_at")


class TopicRetrieveSerializer(TimestampSerializerMixin, AuthorMixin):
    posts = PostListSerializer(many=True, source="latests_posts")

    class Meta:
        model = models.Topic
        fields = ("pk", "name", "title", "url_name", "author", "description", "posts", "created_at", "updated_at")


class TopicSerializer(TimestampSerializerMixin, AuthorCreateMixin):
    url_name = serializers.SlugField(read_only=True)

    class Meta:
        model = models.Topic
        fields = ("name", "title", "url_name", "author", "description", "created_at", "updated_at")


class PostSerializer(TimestampSerializerMixin, AuthorCreateMixin):
    topic = serializers.HiddenField(
        default=NestedObject(lookup="topic_url_name", lookup_field="url_name", model=models.Topic)
    )

    class Meta:
        model = models.Post
        fields = ("pk", "title", "content", "author", "topic", "created_at", "updated_at")


class PostRetrieveSerializer(TimestampSerializerMixin, AuthorMixin):
    topic = TopicListSerializer(read_only=True)

    class Meta:
        model = models.Post
        fields = ("pk", "title", "content", "author", "topic", "created_at", "updated_at")


class CommentSerializer(TimestampSerializerMixin, AuthorCreateMixin):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = serializers.HiddenField(default=NestedObject(lookup="post_pk", lookup_field="pk", model=models.Post))

    class Meta:
        model = models.Comment
        fields = ("pk", "title", "content", "author", "post", "created_at", "updated_at")


class CommentRetrieveSerializer(TimestampSerializerMixin, AuthorMixin):
    post = PostRetrieveSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = ("pk", "title", "content", "author", "post", "created_at", "updated_at")


class CommentListSerializer(TimestampSerializerMixin):
    author = serializers.StringRelatedField()

    class Meta:
        model = models.Comment
        fields = ("pk", "title", "content", "author", "created_at", "updated_at")
