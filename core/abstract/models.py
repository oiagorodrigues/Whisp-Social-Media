import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404


class AbstractManager(models.Manager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404


class AbstractModel(models.Model):
    public_id = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = AbstractManager()

    class Meta:
        """
        An abstract class can be considered a blueprint for other classes. It usually contains a set of methods or attributes that must be created within any child classes built from the abstract class.
        Django will ignore this class model and won't generate migrations for this.
        """

        abstract = True
