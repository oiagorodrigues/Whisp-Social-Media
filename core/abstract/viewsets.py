from rest_framework import viewsets, filters


class AbstractViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.OrderingFilter]
    # This list contains the fields that can be used as ordering parameters when making a request.
    ordering_fields = ["updated", "created"]
    ordering = ["-updated"]
