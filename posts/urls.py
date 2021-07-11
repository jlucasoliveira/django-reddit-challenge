from django.conf.urls import include
from django.urls import path

from posts.api.v1.routes import comment_router, post_router, topic_router

urlpatterns = [
    path("api/v1/", include(topic_router.urls)),
    path("api/v1/", include(post_router.urls)),
    path("api/v1/", include(comment_router.urls)),
]
