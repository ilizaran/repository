from django.contrib import admin
from django import forms
from record.models import Record, File, TypeRecord, Collection, Place, Acquisition, Author, SelectFile
from record.forms import SelectFileForm, RecordForm


class FileAdminInline(admin.TabularInline):
    exclude = ()
    model = File
    max_num = 10000
    search_fields = ('filebrowse', )
    ordering = ('filebrowse', )

class SelectFileInline(admin.StackedInline):
    form = SelectFileForm
    model = SelectFile
    max_num = 1
    extra = 1

class RecordAdmin(admin.ModelAdmin):
    exclude = ()
    inlines = [SelectFileInline,FileAdminInline,]
    form = RecordForm
    search_fields = ('name', 'signature', 'identificador' )
    list_filter = ('collection',)
    list_display = ('name', 'signature', 'identificador','id','date' )
    filter_horizontal = ('author',)

class FileTypeAdmin(admin.ModelAdmin):
    exclude = ()
    search_fields = ('name', )

class FileAdmin(admin.ModelAdmin):
    exclude = ()
    search_fields = ('filebrowse', )
    ordering = ('filebrowse', )

class TypeRecordAdmin(admin.ModelAdmin):
    exclude = ()
    search_fields = ('name', )
    ordering = ('name', )

class CollectionAdmin(admin.ModelAdmin):
    exclude = ()
    search_fields = ('name',)
    ordering = ('name',)

class PlaceAdmin(admin.ModelAdmin):
    exclude = ()
    search_fields = ('name',)
    ordering = ('name',)

class AuthorAdmin(admin.ModelAdmin):
    exclude = ()
    search_fields = ('name',)
    ordering = ('name',)

class AcquisitionAdmin(admin.ModelAdmin):
    exclude = ()
    search_fields = ('name',)
    ordering = ('name',)


admin.site.register(Record, RecordAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(TypeRecord, TypeRecordAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Acquisition, AcquisitionAdmin)
admin.site.register(Author, AuthorAdmin)
