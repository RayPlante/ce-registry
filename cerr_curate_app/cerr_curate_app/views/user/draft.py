"""
The module that provides the user views for creating and editing a draft record.  
"""
from collections import OrderedDict

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .forms import StartForm, EditForm

# from ..components.draft import Draft
class Draft():
    name = None
    id = None
    data = None
    file = None
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])


TMPL8S = 'cerr_curate_app/user/draft/'

def start(request):
    """
    Present or handle the starting form for creating a record
    """
    if request.method == 'POST':
        form = StartForm(request.POST, request.FILES)
        if form.is_valid():
            draft = start_to_draft(form.cleaned_data, request.FILES.get('xmlfile'))
            id = save_new_draft(draft)
            return HttpResponseRedirect(reverse('edit', args=(id,)))

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
            draft = edit_to_draft(form.cleaned_data)
            save_draft_as(draft, draft_id)
            return HttpResponseRedirect(reverse('start'))

    else:
        draft = get_draft(draft_id)
        form = EditForm(initial=draft_to_edit(draft))

    return render(request, TMPL8S+'edit.html',
                  { 'recname': draft.name, 'editform': form, 'draft_id': draft_id })

def start_to_draft(startdata, file_submission=None):
    # replace this implementation with use of a real Draft model
    draft = OrderedDict([('identity', OrderedDict()),
                         ('content',  OrderedDict())])
    if file_submission is None or startdata['start_meth'] == 'create':
        if startdata['create'].get('homepage'):
            draft['content']['landingPage'] = startdata['create'].get('homepage')
        return Draft(name=startdata['create']['name'], data=draft)

    return Draft(name=file_submission.name, data=draft, file=file_submission)

def draft_to_edit(draft):
    return {'homepage': draft.data.get('content', {}).get('landingPage','')}

def edit_to_draft(data):
    draft = OrderedDict([('identity', OrderedDict()),
                         ('content',  OrderedDict())])
    if data.get('homepage'):
        draft['content']['landingPage'] = data.get('homepage','')
    return Draft(data=draft)


_drafts = []
def save_new_draft(draft):
    # replace this implementation with use of a real Draft model
    global _drafts
    id = len(_drafts)
    draft.id = str(id)
    _drafts.append(draft)
    return draft.id

def get_draft(id):
    global _drafts
    try:
        return _drafts[int(id)]
    except (IndexError, TypeError) as ex:
        raise Http404("Draft ID not found")

def save_draft_as(draft, id):
    old = get_draft(id)
    try:
        old.data = draft.data
        _drafts[int(id)] = draft
    except (IndexError, ValueError) as ex:
        raise Http404("Draft ID not found")
