"""Curate registry app user views
"""
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View

import core_curate_app.permissions.rights as rights
import core_main_app.utils.decorators as decorators
from core_curate_registry_app.settings import REGISTRY_XSD_FILENAME
from core_main_app.commons import exceptions
from core_main_app.components.version_manager import api as version_manager_api
from core_main_app.components.template import api as template_api
from core_main_app.utils.rendering import render
from core_main_registry_app.components.custom_resource import api as custom_resource_api
from cerr_curate_app.components.cerrdata.models import CerrData
from cerr_curate_app.components.cerrdata import api as cerrdata_api

from xml.etree.ElementTree import Element,tostring
from core_main_app.components.version_manager import api as version_manager_api
from core_main_app.components.version_manager.models import VersionManager

from .forms import  NameForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from core_main_registry_app.components.category import api as category_api
from cerr_curate_app.components.draft import api as draft_api

def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('/curate?submitted=True')
    else :

        context = {}
        context['form'] = NameForm()
        return render(
            request,
            "cerr_curate_app/user/curate.html",
            context=context
        )


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cd = form.cleaned_data
            form_string = render_xml('Resource', cd, 'active')
            data = CerrData()
            data.title = cd['name']
            version_manager = VersionManager.get_all()
            version_manager = version_manager.filter(_cls='VersionManager.TemplateVersionManager')
            template = template_api.get(str(version_manager[0].current), request)
            data.template = template
            data.user_id = str(request.user.id)            # process the data in form.cleaned_data as required
            # set content
            data.xml_content = form_string
            # save data
            data = cerrdata_api.upsert(data, request)

            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/curate?submitted=True')

    # if a GET (or any other method) we'll create a blank form
    else:

        form = NameForm()

    return render(request, 'cerr_curate_app/user/curate.html', context= {'form': form})


def save_as_draft(request):
    form=NameForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        form_string = render_xml('Resource', cd, 'active')
        version_manager = VersionManager.get_all()
        version_manager = version_manager.filter(_cls='VersionManager.TemplateVersionManager')
        template = template_api.get(str(version_manager[0].current), request)
        draft_api.dict_to_string(cd)

class StartCurate(View):
    """Start curate."""

    def __init__(self):
        super(StartCurate, self).__init__()
        self.assets = {
            "js": [
                {"path": "core_curate_app/user/js/select_template.js", "is_raw": False},
                {
                    "path": "core_curate_registry_app/user/js/start_curate.js",
                    "is_raw": False,
                },
            ],
            "css": ["core_curate_app/user/css/style.css"],
        }
        self.modals = []

    @method_decorator(
        decorators.permission_required(
            content_type=rights.curate_content_type,
            permission=rights.curate_access,
            login_url=reverse_lazy("core_main_app_login"),
        )
    )
    def get(self, request, role):
        """Start curate with role parameter.
        Args:
            request:
            role:

        Returns:
        """
        try:
            # Get custom resources for the current template
            custom_resource = custom_resource_api.get_by_current_template_and_slug(
                role, request=request
            )
        except exceptions.DoesNotExist:
            custom_resource = None

        context = {
            "template_id": version_manager_api.get_active_global_version_manager_by_title(
                REGISTRY_XSD_FILENAME, request=request
            ).current,
            "role": role,
            "custom_resource": custom_resource,
        }
        return render(
            request,
            "core_curate_app/user/curate.html",
            assets=self.assets,
            modals=self.modals,
            context=context,
        )


def render_xml(tag,clean_data, status):
    elem = Element(tag)
    elem.set('status', status)
    for key, val in clean_data.items():
        # create an Element
        # class object
        child = Element(key)
        child.text = str(val)
        elem.append(child)

    return tostring(elem)

