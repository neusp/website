# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from cms.models import MenuItem, MenuSubitem
from django.shortcuts import render_to_response, get_object_or_404

def main(request):
    return render_to_response('base.html', {})
    #return HttpResponse(request.path)
    #raise Http404()
