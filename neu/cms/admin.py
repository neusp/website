# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from cms.models import *

class MenuSubitemFormSet(forms.models.BaseInlineFormSet):
    def clean(self):
        orders = []
        for form in self.forms:
            if any(form._errors):
                return
        for form in self.forms:
            order = form.cleaned_data.get('order')
            if order:
                orders.append(order)
        if sorted(orders) != range(1, len(orders) + 1):
            raise forms.ValidationError('Subitens do menu devem ter ordens distintas\
                                         e sucessivas a partir de 1.')


class MenuSubitemInline(admin.StackedInline):
    model = MenuSubitem
    formset = MenuSubitemFormSet


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'color',)
    inlines = [MenuSubitemInline]


class NavigationMenuItemInline(admin.StackedInline):
    model = NavigationMenuItem


class NavigationMenuAdmin(admin.ModelAdmin):
    inlines = [NavigationMenuItemInline]


class TemplateInline(admin.StackedInline):
    model = Template


class PageAdmin(admin.ModelAdmin):
    list_diplay = ('name', 'url')
    inlines = [TemplateInline]


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(NavigationMenu, NavigationMenuAdmin)
