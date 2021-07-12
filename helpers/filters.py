from __future__ import annotations

from typing import Type

from rest_framework import filters

from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.views import View


class NestedFilter(filters.BaseFilterBackend):
    def filter_queryset(
        self: NestedFilter,
        request: HttpRequest,
        queryset: QuerySet,
        view: Type[View],
    ) -> QuerySet:
        url_kwarg = getattr(view, "parent_url_kwarg")
        lookup = getattr(view, "parent_url_field", "pk")
        value = view.kwargs.get(f"{url_kwarg}_{lookup}")
        return queryset.filter(**{f"{url_kwarg}__{lookup}": value})
