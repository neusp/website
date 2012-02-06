from django.contrib import admin
from cms.models import *

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'color')


class TemplateInline(admin.StackedInline):
    model = Template


class PageAdmin(admin.ModelAdmin):
    list_diplay = ('name', 'url')
    inlines = [TemplateInline]


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'institute')


admin.site.register(Person, PersonAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(RegisterFormPosition)
admin.site.register(TemplateType)
admin.site.register(MenuItem, MenuItemAdmin)
