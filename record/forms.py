# -*- encoding: utf-8 -*-
from django import forms
from filebrowser.fields import FileBrowseField
from django.conf import settings
from record.models import Record,SelectFile

class KindEditor(forms.Textarea):
    class Media:
        css ={
            'all':(settings.STATIC_URL+'kindeditor/themes/default/default.css',)
        }
        js = (settings.STATIC_URL+'kindeditor/kindeditor-all-min.js',settings.STATIC_URL+'kindeditor/evento.js',settings.STATIC_URL+'kindeditor/lang/en.js',)
    def __init__(self, attrs = {}):
        attrs['class'] = 'mykindeditor'
        super(KindEditor, self).__init__(attrs)

class RecordForm(forms.ModelForm):
    description = forms.CharField( widget=KindEditor(attrs={'rows': 3, 'cols': 80}),required=False)

    class Meta:
        model = Record
        exclude = []

class SelectFileForm(forms.ModelForm):
    #patron = forms.CharField(label='Patron de selección de ficheros (eje. *.jpg)')

    class Meta:
        model=SelectFile
        exclude = []
