from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from core_main_app.components.template.models import Template
from django_mongoengine import fields
from mongoengine import errors as mongoengine_errors
from core_main_app.commons import exceptions
import logging

logger = logging.getLogger(__name__)


class Circular(MPTTModel):
    # schema associated with the draft document
    template = fields.ReferenceField(Template)
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ["name"]



    @staticmethod
    def get_by_id(circular_id):
        """Return the object with the given id.

        Args:
            circular_id:

        Returns:
            Circular (obj): Circular object with the given id

        """
        try:
            return Circular.objects.get(pk=str(circular_id))
        except mongoengine_errors.DoesNotExist as e:
            raise exceptions.DoesNotExist(str(e))
        except Exception as ex:
            raise exceptions.ModelError(str(ex))

    @staticmethod
    def get_all():
        """Get all Circulars

        Returns:

        """
        return Circular.objects.all()
