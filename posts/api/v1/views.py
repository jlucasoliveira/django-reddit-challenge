from __future__ import annotations

from rest_framework import viewsets
from rest_framework.serializers import Serializer

from posts import models
from posts.api.v1 import serializers as api_serializers


class TopicViewSet(viewsets.ModelViewSet):
    lookup_field = "url_name"
    lookup_url_kwarg = "url_name"
    queryset = models.Topic.objects.select_related("author")  # .prefetch_related("posts")
    serializer_class = api_serializers.TopicSerializer

    def get_serializer_class(self: TopicViewSet) -> Serializer:
        if self.action in ["list", "retrieve"]:
            return api_serializers.TopicListSerializer
        return super().get_serializer_class()
