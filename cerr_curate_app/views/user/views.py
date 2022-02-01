"""Curate registry app user views
"""

from django.http import HttpResponseRedirect
from django.shortcuts import render

from cerr_curate_app.components.cerrdata import api as cerrdata_api
from core_main_app.utils.rendering import render
from .forms import NameForm


def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('/curate?submitted=True')
    else:

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
            data = cerrdata_api.save_as_cerr_data(request)
            # redirect to a new URL:
            return HttpResponseRedirect('/curate?submitted=True')

    # if a GET (or any other method) we'll create a blank form
    else:

        form = NameForm()

    return render(request, 'cerr_curate_app/user/curate.html', context={'form': form})


