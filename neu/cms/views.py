# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from cms.models import Page, MenuItem, MenuSubitem
from django.shortcuts import render_to_response, get_object_or_404

def main(request):
    menu_items = MenuItem.objects.all()
    page = get_object_or_404(Page, url=request.path)
    menu_item = page.menus.get()
    return render_to_response('base.html',
                              {'menu_items': menu_items,
                               'page': page,
                               'menu_item': menu_item})
    #return HttpResponse(request.path)
    #raise Http404()
