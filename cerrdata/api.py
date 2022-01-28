import core_main_app.access_control.api
import core_main_app.components.workspace.access_control
from core_main_app.access_control.decorators import access_control
from core_main_app.commons import exceptions as exceptions

from core_main_app.utils.xml import validate_xml_data
from xml_utils.xsd_tree.xsd_tree import XSDTree
from cerr_curate_app.components.cerrdata.models import CerrData


@access_control(core_main_app.access_control.api.can_request_write)
def upsert(data, request):
    """Save or update the data.

    Args:
        data:
        request:

    Returns:

    """
    if data.xml_content is None:
        raise exceptions.ApiError("Unable to save data: xml_content field is not set.")

    check_xml_file_is_valid(data, request=request)
    return data.cerr_convert_and_save()



def check_xml_file_is_valid(data, request=None):
    """Check if xml data is valid against a given schema.

    Args:
        data:
        request:

    Returns:

    """
    template = data.template

    try:
        xml_tree = XSDTree.build_tree(data.xml_content)
    except Exception as e:
        raise exceptions.XMLError(str(e))
    try:
        xsd_tree = XSDTree.build_tree(template.content)
    except Exception as e:
        raise exceptions.XSDError(str(e))
    error = validate_xml_data(xsd_tree, xml_tree, request=request)
    if error is not None:
        raise exceptions.XMLError(error)
    else:
        return True


