from rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

from posts import models


class TopicListSerializer(serializers.ModelSerializer):
    author = UserDetailsSerializer(read_only=True)

    class Meta:
        model = models.Topic
        fields = ("pk", "name", "title", "url_name", "author", "description", "created_at", "updated_at")


class TopicSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Topic
        fields = ("name", "title", "author", "description")
