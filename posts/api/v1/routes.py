from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from posts.api.v1 import views as api_views

topic_router = SimpleRouter()
topic_router.register("topics", api_views.TopicViewSet, basename="topics")


post_router = NestedSimpleRouter(topic_router, "topics", lookup="topic")
post_router.register("posts", api_views.PostViewSet, basename="posts")
