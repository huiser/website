from django.shortcuts import render_to_response
from django.template.context import RequestContext

from bootstrap_toolkit.widgets import BootstrapUneditableInput

def home(request):
    return render_to_response('home.html', RequestContext(request, {}))
