from __future__ import annotations

from typing import Any, Dict

from rest_framework import viewsets

from helpers import filters as api_filters


class NestedModelViewSet(viewsets.ModelViewSet):
    filter_backends = (api_filters.NestedFilter,)

    def get_serializer_context(self: NestedModelViewSet) -> Dict[str, Any]:
        context = super().get_serializer_context()
        context.update({"kwargs": self.kwargs})
        return context
