from rest_framework.routers import SimpleRouter

from topic.api.v1 import views as api_views

topic_router = SimpleRouter()
topic_router.register("topics", api_views.TopicViewSet, basename="topics")
