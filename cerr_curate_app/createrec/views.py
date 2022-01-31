import pdb

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from .forms import StartForm

# Create your views here.
def start(request):
    """
    Present or handle the starting form for creating a record
    """
    if request.method == 'POST':
        form = StartForm(request.POST, request.FILES)
        if form.is_valid():
            ctx = form.cleaned_data
            ctx['errors'] = form.create.errors
            return render(request, 'createrec/show.html', ctx)

    else:
        form = StartForm()

    return render(request, 'createrec/index.html', { 'startform': form })

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



    
