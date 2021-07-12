from __future__ import annotations

from rest_framework.serializers import Serializer

from comment import models
from comment.api.v1 import serializers as api_serializers
from helpers.views import NestedModelViewSet


class CommentViewSet(NestedModelViewSet):
    parent_url_kwarg = "post"
    queryset = models.Comment.objects.select_related("author")
    serializer_class = api_serializers.CommentSerializer

    def get_serializer_class(self: CommentViewSet) -> Serializer:
        if self.action == "retrieve":
            return api_serializers.CommentRetrieveSerializer
        if self.action == "list":
            return api_serializers.CommentListSerializer
        return super().get_serializer_class()
