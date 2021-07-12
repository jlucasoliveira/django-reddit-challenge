"""
backend-challenge-001 URL Configuration
"""
###
# Libraries
###
from django.conf.urls import include, url
from django.contrib import admin

from helpers.health_check_view import health_check

###
# URLs
###
urlpatterns = [
    # Admin
    url(r"^admin/", admin.site.urls),
    # Health Check
    url(r"health-check/$", health_check, name="health_check"),
    # Applications
    url(r"^", include("accounts.urls")),
    url(r"^", include("topic.urls")),
    url(r"^", include("post.urls")),
    url(r"^", include("comment.urls")),
]
