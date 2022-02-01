import pdb

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from createrec.views import drafts

# Create your views here.
def edit(request, draft_id):
    data = get_draft(draft_id)
    ctx = { 'start_meth': 'create', 'create': { 'name': draft_id, 'homepage': data.get('landingPage') } }
    return render(request, 'createrec/show.html', ctx)

def get_draft(draft_id):
    if draft_id not in drafts:
        raise Http404("Draft not found")

    draft = drafts[draft_id]
    return { 'landingPage': draft.get('content', {}).get('landingPage', '') }
    
