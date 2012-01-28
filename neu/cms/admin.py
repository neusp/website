# -*- coding: utf-8 -*-

from django.contrib import admin
from cms.models import MenuItem, SubMenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'color',)

class SubMenuItemInline(admin.StackedInline):
    model = SubMenuItem

admin.site.register(MenuItem, MenuItemAdmin, inlines=[SubMenuItemInline])
