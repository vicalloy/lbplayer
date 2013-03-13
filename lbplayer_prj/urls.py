from django.conf.urls.defaults import patterns, url, include
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#from filebrowser.sites import site

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    #url(r'^admin/filebrowser/', include(site.urls)),
    #(r'^grappelli/',include('grappelli.urls')),

    url(r'^', include('lbplayer.urls')),
)

from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
