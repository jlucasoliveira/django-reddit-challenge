from rest_framework_nested.routers import NestedSimpleRouter

from comment.api.v1 import views as api_views
from post.api.v1.routes import post_router

comment_router = NestedSimpleRouter(post_router, "posts", lookup="post")
comment_router.register("comments", api_views.CommentViewSet, basename="comments")
