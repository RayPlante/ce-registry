from django.http.response import HttpResponseBadRequest, HttpResponse

from core_main_app.access_control.exceptions import AccessControlError
from core_main_app.commons.exceptions import DoesNotExist
from cerr_curate_app.views.user.forms.roles import roleForm, softwareRoleForm, serviceApiForm, defaultRoleForm


def role_form(request):
    """Endpoint for role form value

    :param request:
    :return:
    """
    if request.method == "GET":
        return get_role_form(request)
    elif request.method == "POST":
        return save_role_form(request)

def get_role_form(request):
    """Gets the value of a data structure element

    Args:
        request:

    Returns:

    """
    if "ajax_get_role" not in request.GET:
        return HttpResponseBadRequest()

    try:
        #Create form instance
        newform = roleForm.createForm(request.ajax_get_role,request.data)
        #Create html
        html_form = newform.render()
        return HttpResponse(html_form)

    except (AccessControlError, DoesNotExist) as exc:
        return HttpResponseBadRequest(json.dumps({"message": str(exc)}))


def save_role_form(request):

    """Post value """
    pass