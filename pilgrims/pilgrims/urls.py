from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.home', name='home'),
    # url(r'^pilgrims/', include('pilgrims.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    ## Third party helpers
    (r'^tinymce/', include('tinymce.urls')),
    # (r'^newsletter/', include('newsletter.urls')),
)
