# -*- coding: utf-8 -*-
from django.shortcuts import render
from record.models import Collection, TypeRecord, Record, File, Place, Author
from django import forms
import django_tables2 as tables
import django_filters
from django_tables2   import RequestConfig
from django.urls import reverse
from django.utils.safestring import mark_safe

class busquedaForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=230)

class RecordTable(tables.Table):
    identificador = tables.Column(orderable=True)
    name = tables.Column(orderable=True)
    signature = tables.Column(orderable=True)
    collection=tables.Column(orderable=False)
    typerecord = tables.Column(orderable=False)
    place = tables.Column(orderable=True)

    def render_identificador(self, value):
        url = reverse("mostrar_registro", args=(str(value),))
        return mark_safe(u'<a href="%s">%s</a>' %(url,  str(value)))

    class Meta:
        attrs = {'class': 'table table-striped'}

class RecordFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    signature = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.ChoiceFilter(choices=(Author.objects.all().order_by('name').values_list('id', 'name')))

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
            super(RecordFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
            self.filters['collection'].field.widget.attrs.update({'class': 'form-select'})
            self.filters['name'].field.widget.attrs.update({'class': 'form-control'})
            self.filters['signature'].field.widget.attrs.update({'class': 'form-control'})
            self.filters['description'].field.widget.attrs.update({'class': 'form-control'})
            self.filters['author'].field.widget.attrs.update({'class': 'form-select'})
            self.filters['place'].field.widget.attrs.update({'class': 'form-select'})
            self.filters['typerecord'].field.widget.attrs.update({'class': 'form-select'})

    class Meta:
        model = Record
        # exclude = ['identificador','fileico','date','acquisition']
        fields=['author','collection','place','typerecord']
        #order_by_field = ['author__name']

def inicio(request,template_name='inicio.html'):
    registros = Record.objects.all()
    fregistros = RecordFilter(request.GET, queryset=registros)
    print(fregistros)
    if len(request.GET)>0:
        if fregistros.qs.count():
            table=RecordTable(fregistros.qs)
            RequestConfig(request, paginate={"per_page": 30}).configure(table)
            return render(request,template_name, {'formulario':fregistros,'table':table})
        else:
            return render(request,template_name, {'formulario':fregistros,'nada':'No se han encontrado registros coincidentes.'})

    colecciones = Collection.objects.all().order_by('name')
    tipos = TypeRecord.objects.all().order_by('name')
    nregistros = Record.objects.all().count()
    ficheros = File.objects.all().count()
    lugares = Place.objects.all().order_by('name')
    return render(
        request,
        template_name,
        {
        'lugares':lugares,
        'colecciones': colecciones,
        'tipos': tipos,
        'registros':nregistros,
        'ficheros':ficheros,
        'formulario':fregistros,
        }
        )
