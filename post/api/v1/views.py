from __future__ import annotations

from rest_framework.serializers import Serializer

from helpers.views import NestedModelViewSet
from post import models
from post.api.v1 import serializers as api_serializers


class PostViewSet(NestedModelViewSet):
    parent_url_kwarg = "topic"
    parent_url_field = "url_name"
    queryset = models.Post.objects.select_related("author")
    serializer_class = api_serializers.PostSerializer

    def get_serializer_class(self: PostViewSet) -> Serializer:
        if self.action == "list":
            return api_serializers.PostListSerializer
        if self.action == "retrieve":
            return api_serializers.PostRetrieveSerializer
        return super().get_serializer_class()
