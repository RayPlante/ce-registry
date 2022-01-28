import logging
from abc import abstractmethod

from django_mongoengine import fields, Document

from core_main_app.commons import exceptions
from core_main_app.components.template.models import Template
from core_parser_app.components.data_structure_element.models import (
    DataStructureElement,
)
from core_parser_app.tasks import delete_branch_task
from core_main_app.components.data.models import Data
from mongoengine.queryset.base import CASCADE

logger = logging.getLogger(__name__)


class Draft(Document):
    """Stores data being entered and not yet curated"""

    user = fields.StringField()
    template = fields.ReferenceField(Template)
    name = fields.StringField(unique_with=["user", "template"])
    form_string = fields.StringField(blank=True)
    data = fields.ReferenceField(Data, blank=True, reverse_delete_rule=CASCADE)

    meta = {"abstract": True}

