from django.contrib import admin
from cms.models import *

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'color',)


class TemplateInline(admin.StackedInline):
    model = Template


class PageAdmin(admin.ModelAdmin):
    list_diplay = ('name', 'url')
    inlines = [TemplateInline]


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Page, PageAdmin)
