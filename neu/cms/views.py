from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from cms.models import Page, MenuItem
from cms.forms import RegisterForm

def main(request):
    if request.path[-1] != '/':
        return HttpResponseRedirect(request.path + '/')
    saved = False
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            saved = True
    else:
        register_form = RegisterForm()
    dict = {}
    dict.update(csrf(request))
    page = get_object_or_404(Page, url=request.path)
    dict['page'] = page
    dict['menu_item'] = get_object_or_404(MenuItem, page=page)
    dict['templates'] = page.templates.all()
    dict['menu_items'] = MenuItem.objects.all()
    dict['register_form'] = register_form
    dict['saved'] = saved
    return render_to_response('base.html', dict)
