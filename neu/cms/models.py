# -*- coding: utf-8 -*-

from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError

class Page(models.Model):
    name = models.CharField(
        'Nome',
        max_length=128
    )
    url = models.CharField(
        'URL',
        max_length=128,
        unique=True,
        validators=[validators.RegexValidator('^[a-zA-Z0-9_/]+$', 'String inválida.')],
        help_text="String que será utilizada na url. Apenas caracteres\
                   alfanuméricos, _' e '/' são permitidos."
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Página'
    
    def __unicode__(self):
        return u'%s' % (self.name,)


class NavigationMenu(models.Model):
    name = models.CharField(
        'Nome',
        max_length=128
    )

    class Meta:
        verbose_name = 'Menu de navegação'
        verbose_name_plural = 'Menus de navegação'

    def __unicode__(self):
        return u'%s' % (self.name,)


class NavigationMenuItem(models.Model):
    name = models.CharField(
        'Nome',
        max_length=128,
        help_text='Texto que será colocado no menu de navegação.'
    )
    navigation_menu = models.ForeignKey(
        NavigationMenu,
        verbose_name='Menu de navegação',
        related_name='itens'
    )
    page = models.ForeignKey(
        Page,
        verbose_name='Página'
    )
    selected = models.BooleanField(
        'Selecionado',
        default=False
    )
    order = models.IntegerField(
        'Ordem',
        help_text='Ordem do item no menu de navegação.'
    )

    class Meta:
        verbose_name = 'Item do menu de navegação'
        verbose_name_plural = 'Itens do menu de navegação'

    def __unicode__(self):
        return u'%s - %s' % (unicode(self.navigation_menu), self.name)


class Template(models.Model):
    name = models.CharField(
        'Nome',
        max_length=128
    )
    title = models.CharField(
        'Título',
        max_length=128,
    )
    text = models.TextField('Texto')
    image = models.ImageField(
        'Imagem de fundo',
        upload_to='images',
        max_length=1000000
    )
    page = models.ForeignKey(
        Page,
        verbose_name='Página',
        related_name='templates'
    )
    order = models.IntegerField(
        'Ordem',
        help_text='Ordem do template na página.'
    )
    navigation_menu = models.ForeignKey(
        NavigationMenu,
        verbose_name='Menu de navegação',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Template'

    def __unicode__(self):
        return u'%s' % (self.name,)


class MenuItem(models.Model):
    name = models.CharField(
        'Nome',
        max_length=128,
        help_text='Texto que será colocado no menu.'
    )
    page = models.ForeignKey(
        Page,
        verbose_name='Página',
        blank=True,
        null=True
    )
    color = models.CharField(
        'Cor',
        max_length=128,
        choices=(
            ('blue', 'Azul'),
            ('yellow', 'Amarelo'),
            ('pink', 'Rosa'),
            ('orange', 'Laranja')
        ),
        help_text='Cor que será utilizada no menu.'
    )
    order = models.IntegerField(
        'Ordem',
        unique=True,
        help_text='Ordem do item no menu.'
    )

    class Meta:
        ordering = ('order',)
        verbose_name = 'Item do menu'
        verbose_name_plural = 'Itens do menu'

    def __unicode__(self):
        return u'%s' % (self.name,)


class MenuSubitem(models.Model):
    menu_item = models.ForeignKey(
        MenuItem,
        verbose_name='Menu',
        related_name='subitems'
    )
    name = models.CharField(
        'Nome',
        max_length=128,
        help_text='Texto que será colocado no submenu.'
    )
    page = models.ForeignKey(
        Page,
        verbose_name='Página'
    )
    order = models.IntegerField('Ordem')

    class Meta:
        verbose_name = 'Subitem do menu'
        verbose_name_plural = 'Subitens do menu'

    def __unicode__(self):
        return u'%s' % (self.name,)
