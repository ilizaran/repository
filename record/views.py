from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from record.models import Record, File, Collection, TypeRecord, Place


def mostrar_registro(request, idt, template_name='mostrar_registro.html'):
	registro = get_object_or_404(Record, identificador=idt)
	ficheros = File.objects.filter(record=registro).order_by('group','filebrowse')

	return render(request,template_name, {'registro': registro,'ficheros': ficheros})


def listado_por_coleccion(request,col, template_name="listado_por_coleccion.html"):
    coleccion = get_object_or_404(Collection, id=col)
    registros = Record.objects.filter(collection=col).order_by('name')

    return render(request,template_name, {'registros': registros,'coleccion': coleccion})


def listado_por_tipo_material(request,mat, template_name="listado_por_tipo_material.html"):
    tipomaterial = get_object_or_404(TypeRecord, id=mat)
    registros = Record.objects.filter(typerecord=mat).order_by('name')

    return render(request,template_name, {'registros': registros,'tipomaterial': tipomaterial})

def listado_por_lugares(request,lu, template_name="listado_por_lugares.html"):
    lugares = get_object_or_404(Place, id=lu)
    registros = Record.objects.filter(place=lu).order_by('name')

    return render(request,template_name, {'registros': registros,'lugares': lugares})
