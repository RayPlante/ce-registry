from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader


# Create your views here.
def index(request):
    """
    Create the starting form for creating a record
    """
    return render(request, 'createrec/index.html', {})

def start(request):
    """
    Accept a start request, create a new record, and start editing it
    """
    print("processing start")
    raise Http404("Not yet implemented")

