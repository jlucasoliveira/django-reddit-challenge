from django.conf.urls import include
from django.urls import path

from comment.api.v1.routes import comment_router

urlpatterns = [
    path("api/v1/", include(comment_router.urls)),
]
