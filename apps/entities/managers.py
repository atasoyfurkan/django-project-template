from django.db import models
from django.db.models import Count


class OriginManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            _hero_count=Count("hero", distinct=True),
            _villain_count=Count("villain", distinct=True),
        )
        return queryset
