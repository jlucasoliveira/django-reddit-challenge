from rest_framework import serializers

from comment import models
from helpers.serializers import AuthorCreateMixin, AuthorMixin, NestedObject, TimestampSerializerMixin
from post import models as post_models
from post.api.v1.serializers import PostRetrieveSerializer


class CommentSerializer(TimestampSerializerMixin, AuthorCreateMixin):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = serializers.HiddenField(default=NestedObject(lookup="post_pk", lookup_field="pk", model=post_models.Post))

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
