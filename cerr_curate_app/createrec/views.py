import pdb
from collections import OrderedDict

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .forms import StartForm

# Create your views here.
def start(request):
    """
    Present or handle the starting form for creating a record
    """
    if request.method == 'POST':
        form = StartForm(request.POST, request.FILES)
        if form.is_valid():
            id = process_create_request(form.cleaned_data, request.FILES.get('xmlfile'))
            return HttpResponseRedirect(reverse('editrec:edit', args=(id,)))

    else:
        form = StartForm()

    return render(request, 'createrec/index.html', { 'startform': form })

drafts = {}
def process_create_request(reqdata, file_submission=None):
    global drafts
    draft = OrderedDict([('identity', OrderedDict()),
                         ('content',  OrderedDict())])
    if file_submission is None or reqdata['start_meth'] == 'create':
        if reqdata['create'].get('homepage'):
            draft['content']['landingPage'] = reqdata['create'].get('homepage')
        drafts[reqdata['create']['name']] = draft
        return reqdata['create']['name']

    draft['file'] = file_submission
    drafts[file_submission.name] = draft
    return file_submission.name
    
    


def store_post_as_draft(data):
    """
    Given the create data provided by the createrec page, create and store a draft record

    :param dict data:  the POST data delivered by a submitted createrec form
    """
    missing = []

    if not data.get('start_meth'):
        missing.append('start_meth')
    if not data.get('name'):
        missing.append('name')

    if missing:
        raise MissingFormData("createrec.start: Form submission missing required keys: "+str(keys),
                              keys=missing)

    # convert and store data

def harvest_from_url(data, url):
    """
    resolve the given URL and attempt to extract metadata.  If the URL is a DOI URL, pull its DOI metadata.
    If it points to a regular web page, attempt to scrape schema.org metadata.
    """
    return data



    
