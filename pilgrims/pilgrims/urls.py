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
    (r'^newsletter/', include('newsletter.urls')),

    # Django-Registration Auth View Names:
    (r'^accounts/', include('registration.backends.default.urls')),
    # auth_login
    # auth_logout
    # auth_password_change
    # auth_password_change_done
    # auth_password_reset
    # auth_password_reset_confirm
    # auth_password_reset_complete
    # auth_password_reset_done

    # Django-Registration Activation View Names:
    # registration_activation_complete
    # registration_activate'
    # registration_register'
    # registration_complete'
    # registration_disallowed'
)
