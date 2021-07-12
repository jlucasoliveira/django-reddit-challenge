from django.urls import include, path

from topic.api.v1.routes import topic_router

urlpatterns = [
    path("api/v1/", include(topic_router.urls)),
]
