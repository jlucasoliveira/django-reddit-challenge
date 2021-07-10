from django.conf.urls import include
from django.urls import path

from posts.api.v1.routes import router as posts_router

urlpatterns = [
    path("api/v1/", include(posts_router.urls)),
]
