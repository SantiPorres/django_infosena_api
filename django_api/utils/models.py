from django.db import models
from uuid import uuid4

from django.db.models.query import QuerySet

class ActiveManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(
            status = BaseModel.Status.ACTIVE
        )


class BaseModel(models.Model):

    class Status(models.TextChoices):
        ACTIVE = 'Active'
        INACTIVE = 'Inactive'


    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    slug = models.SlugField(
        unique=True,
        default=str(uuid4().hex[:36]),
        max_length=100,
        db_index=True
    )

    status = models.CharField(
        max_length=8,
        choices=Status.choices,
        default=Status.ACTIVE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    objects = models.Manager()

    active = ActiveManager()

    class Meta:
        abstract = True

    def __str__(self):
        return self.slug