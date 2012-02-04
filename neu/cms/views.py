from django.http import HttpResponseRedirect, Http404
from cms.models import Page, MenuItem
from django.shortcuts import render_to_response, get_object_or_404

def main(request):
    if request.path[-1] != '/':
        return HttpResponseRedirect(request.path + '/')
    page = get_object_or_404(Page, url=request.path)
    menu_item = get_object_or_404(MenuItem, page=page)
    templates = page.templates.all()
    menu_items = MenuItem.objects.all()
    return render_to_response('base.html',
                              {'menu_items': menu_items,
                               'page': page,
                               'templates': templates,
                               'menu_item': menu_item})
