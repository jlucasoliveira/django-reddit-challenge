from rest_framework_nested.routers import NestedSimpleRouter

from post.api.v1 import views as api_views
from topic.api.v1.routes import topic_router

post_router = NestedSimpleRouter(topic_router, "topics", lookup="topic")
post_router.register("posts", api_views.PostViewSet, basename="posts")
