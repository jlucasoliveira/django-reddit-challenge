from __future__ import annotations

from typing import Type

from rest_framework import permissions

from django.http.request import HttpRequest
from django.views import View

from helpers.models import AuthorMixin


class IsAuthor(permissions.IsAuthenticated):
    def has_object_permission(
        self: IsAuthor,
        request: HttpRequest,
        view: View,
        obj: Type[AuthorMixin],
    ) -> bool:
        is_safe_method = request.method in permissions.SAFE_METHODS
        is_author = obj.author_id == request.user.id
        return is_safe_method or is_author
