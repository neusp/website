# -*- coding: utf-8 -*-

from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError

class Page(models.Model):
    url = models.CharField(
        'URL',
        max_length=128,
        unique=True,
        validators=[validators.RegexValidator('^[a-zA-Z0-9_/]+$', 'String inválida.')],
        help_text="String que será utilizada na url. Apenas caracteres\
                   alfanuméricos, _' e '/' são permitidos."
    )

    class Meta:
        ordering = ('url',)
        verbose_name = 'Página'
    
    def __unicode__(self):
        return u'%s' % (self.url,)


class Template(models.Model):
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

    class Meta:
        verbose_name = 'Template'

    def __unicode__(self):
        return u'%s' % (self.title,)


class MenuItem(models.Model):
    name = models.CharField(
        'Nome',
        max_length=128,
        help_text='Texto que será colocado no menu.'
    )
    page = models.ForeignKey(
        Page,
        verbose_name='Página',
        related_name='menus',
        blank=True,
        null=True
    )
    color = models.CharField(
        'Cor',
        max_length=128,
        choices=(
            ('#e0e020', 'Amarelo'),
            ('#86b226', 'Verde'),
            ('#f09010', 'Laranja'),
            ('#f01070', 'Rosa'),
            ('#30b0f0', 'Azul')
        ),
        help_text='Cor que será utilizada no menu.'
    )
    order = models.IntegerField(
        'Ordem',
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
