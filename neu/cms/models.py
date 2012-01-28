# -*- coding: utf-8 -*-

from django.db import models
from django.core import validators

class MenuItem(models.Model):
    name = models.CharField(
        "Nome",
        max_length=64,
        help_text="O texto que será colocado no menu."
    )
    url = models.CharField(
        "URL",
        max_length=64,
        validators=[validators.RegexValidator("^[a-zA-Z0-9_]+$", "String inválida")],
        help_text="String que será utilizada na url. Apenas caracteres\
                   alfanuméricos e '_' são permitidos."
    )
    color = models.CharField(
        "Cor",
        max_length=32,
        choices=(
            ('blue', 'Azul'),
            ('yellow', 'Amarelo'),
            ('pink', 'Rosa'),
            ('orange', 'Laranja')
        ),
        help_text="Cor que será utilizada nessa seção do site."
    )
    order = models.IntegerField(
        "Ordem",
        unique=True
    )

    class Meta:
        ordering = ('order',)
        verbose_name = "Item do menu"
        verbose_name_plural = "Itens do menu"

    def __unicode__(self):
        return self.name


class SubMenuItem(models.Model):
    menu_item = models.ForeignKey(
        MenuItem,
        verbose_name="Menu"
    )
    name = models.CharField(
        "Nome",
        max_length=64,
        help_text="O texto que será colocado no submenu."
    )
    url = models.CharField(
        "URL",
        max_length=64,
        validators=[validators.RegexValidator("^[a-zA-Z0-9_]+$", "String inválida")],
        help_text="String que será utilizada na url. Apenas caracteres\
                   alfanuméricos e '_' são permitidos."
    )
    order = models.IntegerField("Ordem")

    class Meta:
        ordering = ('order',)
        verbose_name = 'Subitem do menu'
        verbose_name_plural = 'Subitens do menu'

    def __unicode__(self):
        return self.name
