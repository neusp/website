# -*- coding: utf-8 -*-

from django.contrib import admin
from cms.models import *

class MenuSubitemInline(admin.StackedInline):
    model = MenuSubitem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'color',)
    inlines = [MenuSubitemInline]


class TemplateInline(admin.StackedInline):
    model = Template


class PageAdmin(admin.ModelAdmin):
    list_diplay = ('name', 'url')
    inlines = [TemplateInline]


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Page, PageAdmin)
