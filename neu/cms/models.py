# -*- coding: utf-8 -*-

from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError

class Person(models.Model):
    name = models.CharField(
        'Nome',
        max_length=128
    )
    email = models.EmailField(
        'Email',
        max_length=128,
        unique=True,
    )
    institute = models.CharField(
        'Unidade USP',
        max_length=128,
        blank=True,
        choices=(
            ('EACH', 'Escola de Artes, Ciências e Humanidades'),
            ('ECA', 'Escola de Comunicações e Artes'),
            ('EEFE', 'Escola de Educação Física e Esporte'),
            ('EEFERP', 'Escola de Educação Física e Esporte de Ribeirão Preto'),
            ('EE', 'Escola de Enfermagem'),
            ('EERP', 'Escola de Enfermagem de Ribeirão Preto'),
            ('EEL', 'Escola de Engenharia de Lorena'),
            ('EESC', 'Escola de Engenharia de São Carlos'),
            ('EP', 'Escola Politécnica'),
            ('ESALQ', 'Escola Superior de Agricultura "Luiz de Queiroz"'),
            ('FAU', 'Faculdade de Arquitetura e Urbanismo'),
            ('FCF', 'Faculdade de Ciências Farmacêuticas'),
            ('FCFRP', 'Faculdade de Ciências Farmacêuticas de Ribeirão Preto'),
            ('FD', 'Faculdade de Direito'),
            ('FDRP', 'Faculdade de Direito de Ribeirão Preto'),
            ('FEA', 'Faculdade de Economia, Administração e Contabilidade'),
            ('FEARP', 'Faculdade de Economia, Administração e Contabilidade de Ribeirão Preto'),
            ('FE', 'Faculdade de Educação'),
            ('FFCLRP', 'Faculdade de Filosofia, Ciências e Letras de Ribeirão Preto'),
            ('FFLCH', 'Faculdade de Filosofia, Letras e Ciências Humanas'),
            ('FM', 'Faculdade de Medicina'),
            ('FMRP', 'Faculdade de Medicina de Ribeirão Preto'),
            ('FMVZ', 'Faculdade de Medicina Veterinária e Zootecnia'),
            ('FO', 'Faculdade de Odontologia'),
            ('FOB', 'Faculdade de Odontologia de Bauru'),
            ('FORP', 'Faculdade de Odontologia de Ribeirão Preto'),
            ('FSP', 'Faculdade de Saúde Pública'),
            ('FZEA', 'Faculdade de Zootecnia e Engenharia de Alimentos'),
            ('IAU', 'Instituto de Arquitetura e Urbanismo de São Carlos'),
            ('IAG', 'Instituto de Astronomia, Geofísica e Ciências Atmosféricas'),
            ('IB', 'Instituto de Biociências'),
            ('ICB', 'Instituto de Ciências Biomédicas'),
            ('ICMC', 'Instituto de Ciências Matemáticas e de Computação'),
            ('IEE', 'Instituto de Eletrotécnica e Energia'),
            ('IF', 'Instituto de Física'),
            ('IFSC', 'Instituto de Física de São Carlos'),
            ('IGG', 'Instituto de Geociências'),
            ('IME', 'Instituto de Matemática e Estatística'),
            ('IP', 'Instituto de Psicologia'),
            ('IQ', 'Instituto de Química'),
            ('IQSC', 'Instituto de Química de São Carlos'),
            ('IRI', 'Instituto de Relações Internacionais'),
            ('IO', 'Instituto Oceanográfico'),
        )
    )
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Cadastro'

    def __unicode__(self):
        return u'%s' % (self.name,)


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


class RegisterFormPosition(models.Model):
    y = models.IntegerField('Coordenada vertical do formulário')
    x = models.IntegerField('Coordenada horizontal do formulário')

    class Meta:
        verbose_name = 'Posição do formulário de registro'
        verbose_name_plural = 'Posições do formulário de registro'

    def __unicode__(self):
        return u'(%s, %s)' % (self.y, self.x)


class TemplateType(models.Model):
    name = models.CharField(
        'Nome',
        max_length=128,
    )
    title_y = models.IntegerField('Coordenada vertical do título')
    title_x = models.IntegerField('Coordenada horizontal do título')
    title_size = models.IntegerField(
        'Tamanho da fonte do título',
        help_text='em pixels',
    )
    text_y = models.IntegerField('Coordenada vertical do texto')
    text_x = models.IntegerField('Coordenada horizontal do texto')
    text_width = models.IntegerField('Largura da caixa de texto')
    text_size = models.IntegerField(
        'Tamanho da fonte do texto',
        help_text='em pixels',
    )
    register_form = models.OneToOneField(
        RegisterFormPosition,
        blank=True,
        null=True,
        verbose_name='Formulário de registro'
    )

    class Meta:
        verbose_name = 'Tipo de template'
        verbose_name_plural = 'Tipos de template'

    def __unicode__(self):
        return u'%s' % (self.name,)


class Template(models.Model):
    type = models.ForeignKey(
        TemplateType,
        verbose_name='Tipo',
        help_text='Tipo do template que renderiza a página.'
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
