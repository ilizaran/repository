# -*- coding: utf-8 -*-
from django.db import models
from filebrowser.fields import FileBrowseField

class Collection(models.Model):
    name = models.CharField('Colección', max_length=250)
    description = models.TextField('Descripción', null=True, blank=True)

    def __str__(self):
        return self.name

class TypeRecord(models.Model):
    name = models.CharField('Tipo de documento', max_length=230)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField('Lugar',max_length=250)

    def __str__(self):
        return self.name


class Acquisition(models.Model):
    name = models.CharField('Tipo de adquisición',max_length=250)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField('Autor',max_length=250)
    description = models.TextField('Descripción', null=True, blank=True)

    def __str__(self):
        return self.name

class Record(models.Model):
    name = models.CharField('Nombre', max_length=230)
    identificador = models.CharField('identificador',max_length=20,unique=True)
    signature = models.CharField('Signatura', max_length=40, null=True, blank=True)
    description = models.TextField('Descripción', null=True, blank=True)
    ico = FileBrowseField("Icono", max_length=200, extensions=[".jpg",".png",".jpeg"], blank=True, null=True)
    collection = models.ForeignKey(Collection, verbose_name='Colección', related_name="collection", null=True, blank=True, on_delete=models.RESTRICT)
    typerecord = models.ForeignKey(TypeRecord, verbose_name='Tipo de recurso', related_name="typerecord", null=True, blank=True, on_delete=models.RESTRICT)
    place = models.ForeignKey(Place, verbose_name='Lugar', related_name="place", null=True, blank=True, on_delete=models.RESTRICT)
    author = models.ManyToManyField(Author, verbose_name='Autores', related_name="authors", null=True, blank=True)
    acquisition = models.ForeignKey(Acquisition, verbose_name='Adquisición', related_name="acquisition", null=True, blank=True, on_delete=models.RESTRICT)
    productionDate = models.DateTimeField('Fecha', null=True, blank=True) # Fecha de elaboracion del recurso digital
    date = models.DateTimeField('Fecha',auto_now_add=True)

    def __str__(self):
        return self.name

class File(models.Model):
    filebrowse = FileBrowseField("Fichero", max_length=300, blank=True, null=True)
    group = models.CharField('Grupo', max_length=200, null=True, blank=True)
    record = models.ForeignKey(Record,related_name="files", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.filebrowse


class SelectFileManager(models.Manager):
    def get_queryset(self):
        return super(SelectFileManager, self).get_queryset().none() #No devuelve ningún dato del modelo

class SelectFile(File):
    patron = models.CharField('Patron de selección de ficheros (eje. *.jpg)',blank=False,max_length=30,default="*.jpg")

    objects = SelectFileManager()

    def delete(self):
        pass

    def save(self):
        from django.conf import settings
        import os
        import fnmatch

        try:
            filenames = os.listdir(settings.MEDIA_ROOT +'/'+ self.filebrowse.path)
        except OSError:
            return

        for filename in filenames:
            if os.path.isfile(settings.MEDIA_ROOT +'/'+self.filebrowse.path +'/'+filename) and fnmatch.fnmatch(filename, self.patron):
                from filebrowser.base import FileObject
                fichero=File(record=self.record,group=self.group,filebrowse=FileObject(self.filebrowse.path+'/'+filename))
                fichero.save()
