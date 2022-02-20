"""
The module that provides the user views for creating and editing a draft record.  
"""
from collections import OrderedDict
import json, pdb

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .forms import StartForm, EditForm

from ...components.draft import api as draft_api

TMPL8S = 'cerr_curate_app/user/draft/'

def start(request):
    """
    Present or handle the starting form for creating a record
    """
    if request.method == 'POST':
        form = StartForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                draft = start_to_draftdoc(form.cleaned_data, request.FILES.get('xmlfile'))
                name = draft['name']
                del draft['name']
                draft_obj = draft_api.save_new_draft(draft, name, request)
                return HttpResponseRedirect(reverse('edit', args=(draft_obj.id,)))
            except DetectedFailure as ex:
                return handleFailure(ex)
            except draft_api.AccessControlError as ex:
                return handleFailure(Http401(message=str(ex)))
    else:
        form = StartForm()

    return render(request, TMPL8S+'start.html', { 'startform': form })

def edit(request, draft_id):
    """
    present and accept updates from an editable version of a draft
    On GET, retrieve a requested draft and load it into the edit form.
    On POST, accept the updated draft and save it.
    """
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            try:
                draft = edit_to_draftdoc(form.cleaned_data)
                draft_api.save_updated_draft(draft, draft_id, request)
                return HttpResponseRedirect(reverse('start'))
            except DetectedFailure as ex:
                return handleFailure(ex)
            except draft_api.AccessControlError as ex:
                return handleFailure(Http401(message=str(ex)))

    else:
        try:
            draft_obj = draft_api.get_by_id(draft_id, request.user)
            draft_doc = draft_api.unrender_xml(draft_obj.form_data)
        except draft_api.AccessControlError as ex:
            return handleFailure(Http401(message=str(ex)))
        form = EditForm(initial=draftdoc_to_edit(draft_doc, draft_obj.id))

    return render(request, TMPL8S+'edit.html',
                  { 'recname': draft_obj.name, 'editform': form, 'draft_id': draft_id })

def start_to_draftdoc(startdata, file_submission=None):
    """
    Convert the cleaned data from the form into a draft XML document.  
    :return:  a dictionary containing an "xml_to_dict" representation of the XML document.
    """

    if file_submission is None or startdata['start_meth'] == 'create':
        draft = OrderedDict([
            ("identity", OrderedDict()),
            ("content",  OrderedDict())
        ])
        if startdata['create'].get('homepage'):
            draft['content']['landingPage'] = startdata['create'].get('homepage')
        draft['@status'] = 'active'
        draft = OrderedDict([('Resource', draft), ('name', startdata['create'].get('name'))])
        return draft

    elif file_submission:
        draft = load_uploaded_file(file_submission)
        draft['_name'] = file_submission.name
        return draft

    elif startdata['start_meth'] == 'upload':
        raise Http400("File upload requested but no file was provided")
    else:
        raise Http400("Illegal start method specified")

def uploaded_file_to_draft(filedata):
    raise Http501("not implemented")


def draftdoc_to_edit(draft_doc, draft_id):
    data = {}
    draft = draft_doc.get('Resource',{})
    data['homepage'] = draft.get('content', {}).get('landingPage','')
    data['draft_id'] = draft_id
    return data

def edit_to_draftdoc(data):
    draft = OrderedDict([('identity', OrderedDict()),
                         ('content',  OrderedDict())])
    if data.get('homepage'):
        draft['content']['landingPage'] = data.get('homepage','')
    draft = OrderedDict([('Resource', draft)])
    return draft

def save_new_draft(draftdoc, name, request):
    """
    save a new draft XML document with the given name
    :param dict draftdoc:   the draft XML document as an "xml_to_dict" dictionary
    :param str      name:   the mnemonic name to save the draft under
    :param HttpRequest request:  the HTTP request that delivered the draft; this is used 
                            to authorize the creation of the draft.
    """
    try:
        return draft_api.save_as_draft(draftdoc, name, request).id
    except draft_api.AccessControlError as ex:
        raise Http401("unauthorized")

class DetectedFailure(Exception):
    """
    a base exception used by this module for failures it detects which should result in an
    HTTP response other than 200 or 404.  
    """
    def __init__(self, code, reason=None, message=None):
        if not message:
            message = "%s failure condition detected" % str(code)
            if reason:
                message += ": " + reason
        super(DetectedFailure, self).__init__(message)
        self.status_code = code
        self.reason_phrase = reason

class Http400(DetectedFailure):
    """
    a failure requiring an HTTP response of 400 Bad Request
    """
    def __init__(self, reason=None, message=None):
        super(Http400, self).__init__(400, reason, message)

class Http401(DetectedFailure):
    """
    a failure requiring an HTTP response of 401 Unauthorized 
    """
    def __init__(self, reason=None, message=None):
        super(Http401, self).__init__(401, reason, message)

class Http501(DetectedFailure):
    """
    a failure requiring an HTTP response of 501 Not Implemented
    """
    def __init__(self, reason=None, message=None):
        super(Http501, self).__init__(401, reason, message)

def handleFailure(exc):
    if isinstance(exc, DetectedFailure):
        return HttpResponse(status=exc.status_code, reason=exc.reason_phrase)
