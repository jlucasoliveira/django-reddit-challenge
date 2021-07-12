from django.urls import include, path

from post.api.v1.routes import post_router

urlpatterns = [
    path("api/v1/", include(post_router.urls)),
]
