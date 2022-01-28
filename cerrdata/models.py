from django.db import models
from mongoengine import errors as mongoengine_errors

from core_main_app.commons import exceptions
from core_main_app.utils.validation.regex_validation import not_empty_or_whitespaces
from django_mongoengine import fields, Document
from django.db import models
from django_extensions.db.fields import AutoSlugField
from mptt.models import MPTTModel, TreeForeignKey
from django_mongoengine import fields
from mongoengine import errors as mongoengine_errors
from mongoengine.queryset.base import NULLIFY

from core_main_app.commons import exceptions
from core_main_app.components.abstract_data.models import AbstractData
from core_main_app.components.template.models import Template
from core_main_app.components.workspace.models import Workspace


class CerrData(AbstractData):
    """Data object"""

    template = fields.ReferenceField(Template, blank=False)
    user_id = fields.StringField()
    workspace = fields.ReferenceField(
        Workspace, reverse_delete_rule=NULLIFY, blank=True
    )

    meta = {"indexes": ["title", "last_modification_date", "template", "user_id"]}


    def cerr_convert_and_save(self):
        """Save Data object and convert the xml to dict if needed.

        Returns:

        """
        self.convert_to_dict()
        self.convert_to_file()

        return self.save_object()