from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'bikefinder.views.map'),
    url(r'^map$', 'bikefinder.views.map'),
    #url(r'^map/(.*)$', 'bikefinder.views.map_given'),
    #url(r'^list$', 'bikefinder.views.list'),
    url(r'^poi$', 'bikefinder.views.points_of_intrests'),
    url(r'^submit$', 'bikefinder.views.submit'),
    # url(r'^clebikes/', include('clebikes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
