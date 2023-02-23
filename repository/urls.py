from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site
from repository.views import inicio

admin.autodiscover()

urlpatterns =[
	path('', inicio, name='inicio'),
    path('admin/filebrowser/', site.urls),
    path('admin/', admin.site.urls),
    path('record/', include('record.urls')),
	]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
