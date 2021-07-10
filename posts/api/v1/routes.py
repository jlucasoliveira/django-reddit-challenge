from rest_framework.routers import SimpleRouter

from posts.api.v1 import views as api_views

router = SimpleRouter()
router.register("topics", api_views.TopicViewSet, basename="topics")
