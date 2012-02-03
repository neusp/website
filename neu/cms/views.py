# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from cms.models import Page, MenuItem, MenuSubitem
from django.shortcuts import render_to_response, get_object_or_404

def main(request):
    page = get_object_or_404(Page, url=request.path)
    templates = page.templates.all()
    menu_item = get_object_or_404(MenuItem, page=page)
    menu_items = MenuItem.objects.all()
    return render_to_response('base.html',
                              {'menu_items': menu_items,
                               'page': page,
                               'templates': templates,
                               'menu_item': menu_item})
