#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import fnmatch
import sys
import MySQLdb
import urllib
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "repository.settings")

    django.setup()

    from record.models import Record, File
    from filebrowser.base import FileObject
    import urllib
    print("Carga de ficheros")
    if len(sys.argv)!=5:
        print("Uso: carga-ficheros.py <id-registro> <grupo> <path> <\"patron-fichero\">")
        sys.exit()


    filenames = os.listdir(sys.argv[3])
    try:
        registro = Record.objects.get(id=sys.argv[1])
    except Record.DoesNotExist:
        print("Registro no encontrado")
        sys.exit()

    for filename in filenames:
        if os.path.isfile(sys.argv[3]+'/'+filename) and fnmatch.fnmatch(filename, sys.argv[4]):
            print("CARGAR >> %s id: %s grupo: %s" % (filename,sys.argv[1],sys.argv[2]))
            nombre=sys.argv[3]+'/'+filename
            nombre=nombre.replace('/var/www/datos/','')
            print (nombre)
            fichero=File(record=registro,group=sys.argv[2],filebrowse=FileObject(nombre))
            fichero.save()
