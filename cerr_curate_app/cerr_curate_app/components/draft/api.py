import logging
from xml.etree.ElementTree import Element, tostring

from cerr_curate_app.components.draft import api as draft_api
from cerr_curate_app.components.draft.models import Draft
from core_main_app.access_control.api import can_read, can_write
from core_main_app.access_control.decorators import access_control
from core_main_app.components.template import api as template_api
from core_main_app.components.version_manager.models import VersionManager

logger = logging.getLogger(__name__)

import json


def dict_to_string(dict_data):
    return str(dict_data)


def string_to_dict(dict_string):
    return json.loads(dict_string)


def get_all_by_user_id(user_id):
    """Returns all drafts with the given user

    Args:
        user:
    Returns:
        Draft:
    """
    return Draft.get_all_by_user_id(user_id)


@access_control(can_read)
def get_by_id(draft_id, user):
    """Returns the draft with the given id

    Args:
        draft_id:
        user:

    Returns:

    """
    return Draft.get_by_id(draft_id)


@access_control(can_write)
def upsert(draft, user, id=None):
    """Save or update the draft

    Args:
        Draft:
        user:

    Returns:

    """
    if id:
        # We link the data with the draft then save it
        draft.id = id
        Draft.save_object()
    else:
        return Draft.save_object()


#    if form.is_valid():
def save_as_draft(request, clean_data):
    """
    Takes clean data from a form and saves it as a draft
    :param request:
    :param clean_data:
    :return:
    """

    form_string = render_xml('Resource', clean_data, 'active')
    version_manager = VersionManager.get_all()
    version_manager = version_manager.filter(_cls='VersionManager.TemplateVersionManager')
    template = template_api.get(str(version_manager[0].current), request)
    draft_api.dict_to_string(clean_data)
    draft = Draft(user=request.user, template=template, name=clean_data.name, form_string=form_string)
    draft_api.upsert(draft, request.user)
    return draft


def render_xml(tag, clean_data, status):
    """
    Takes clean data form a form and returns am XML string
    :param tag:
    :param clean_data:
    :param status:
    :return:
    """
    elem = Element(tag)
    elem.set('status', status)
    for key, val in clean_data.items():
        # create an Element
        # class object
        child = Element(key)
        child.text = str(val)
        elem.append(child)

    return tostring(elem)
