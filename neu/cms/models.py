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
        max_length=128
    )
    institute = models.CharField(
        'Unidade USP',
        max_length=128,
        blank=True,
        choices=(
            ('Escola de Artes, Ciências e Humanidades', 'Escola de Artes, Ciências e Humanidades'),
            ('Escola de Comunicações e Artes', 'Escola de Comunicações e Artes'),
            ('Escola de Educação Física e Esporte', 'Escola de Educação Física e Esporte'),
            ('Escola de Educação Física e Esporte de Ribeirão Preto', 'Escola de Educação Física e Esporte de Ribeirão Preto'),
            ('Escola de Enfermagem', 'Escola de Enfermagem'),
            ('Escola de Enfermagem de Ribeirão Preto', 'Escola de Enfermagem de Ribeirão Preto'),
            ('Escola de Engenharia de Lorena', 'Escola de Engenharia de Lorena'),
            ('Escola de Engenharia de São Carlos', 'Escola de Engenharia de São Carlos'),
            ('Escola Politécnica', 'Escola Politécnica'),
            ('Escola Superior de Agricultura "Luiz de Queiroz"', 'Escola Superior de Agricultura "Luiz de Queiroz"'),
            ('Faculdade de Arquitetura e Urbanismo', 'Faculdade de Arquitetura e Urbanismo'),
            ('Faculdade de Ciências Farmacêuticas', 'Faculdade de Ciências Farmacêuticas'),
            ('Faculdade de Ciências Farmacêuticas de Ribeirão Preto', 'Faculdade de Ciências Farmacêuticas de Ribeirão Preto'),
            ('Faculdade de Direito', 'Faculdade de Direito'),
            ('Faculdade de Direito de Ribeirão Preto', 'Faculdade de Direito de Ribeirão Preto'),
            ('Faculdade de Economia, Administração e Contabilidade', 'Faculdade de Economia, Administração e Contabilidade'),
            ('Faculdade de Economia, Administração e Contabilidade de Ribeirão Preto', 'Faculdade de Economia, Administração e Contabilidade de Ribeirão Preto'),
            ('Faculdade de Educação', 'Faculdade de Educação'),
            ('Faculdade de Filosofia, Ciências e Letras de Ribeirão Preto', 'Faculdade de Filosofia, Ciências e Letras de Ribeirão Preto'),
            ('Faculdade de Filosofia, Letras e Ciências Humanas', 'Faculdade de Filosofia, Letras e Ciências Humanas'),
            ('Faculdade de Medicina', 'Faculdade de Medicina'),
            ('Faculdade de Medicina de Ribeirão Preto', 'Faculdade de Medicina de Ribeirão Preto'),
            ('Faculdade de Medicina Veterinária e Zootecnia', 'Faculdade de Medicina Veterinária e Zootecnia'),
            ('Faculdade de Odontologia', 'Faculdade de Odontologia'),
            ('Faculdade de Odontologia de Bauru', 'Faculdade de Odontologia de Bauru'),
            ('Faculdade de Odontologia de Ribeirão Preto', 'Faculdade de Odontologia de Ribeirão Preto'),
            ('Faculdade de Saúde Pública', 'Faculdade de Saúde Pública'),
            ('Faculdade de Zootecnia e Engenharia de Alimentos', 'Faculdade de Zootecnia e Engenharia de Alimentos'),
            ('Instituto de Arquitetura e Urbanismo de São Carlos', 'Instituto de Arquitetura e Urbanismo de São Carlos'),
            ('Instituto de Astronomia, Geofísica e Ciências Atmosféricas', 'Instituto de Astronomia, Geofísica e Ciências Atmosféricas'),
            ('Instituto de Biociências', 'Instituto de Biociências'),
            ('Instituto de Ciências Biomédicas', 'Instituto de Ciências Biomédicas'),
            ('Instituto de Ciências Matemáticas e de Computação', 'Instituto de Ciências Matemáticas e de Computação'),
            ('Instituto de Eletrotécnica e Energia', 'Instituto de Eletrotécnica e Energia'),
            ('Instituto de Física', 'Instituto de Física'),
            ('Instituto de Física de São Carlos', 'Instituto de Física de São Carlos'),
            ('Instituto de Geociências', 'Instituto de Geociências'),
            ('Instituto de Matemática e Estatística', 'Instituto de Matemática e Estatística'),
            ('Instituto de Psicologia', 'Instituto de Psicologia'),
            ('Instituto de Química', 'Instituto de Química'),
            ('Instituto de Química de São Carlos', 'Instituto de Química de São Carlos'),
            ('Instituto de Relações Internacionais', 'Instituto de Relações Internacionais'),
            ('Instituto Oceanográfico', 'Instituto Oceanográfico'),
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
