from django.contrib   import admin
from django.conf.urls import patterns, include, url

import settings
import gestion.api

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$'                        , 'gestion.views.index'),
    url(r'^api/'                     , include(gestion.api.resources.api.urls)),
    url(r'^admin/products/report/$'  , 'gestion.administration.admin_views.product_chart_view'),
    url(r'^tastytools/'              , include('tastytools.urls'), {'api_name': gestion.api.resources.api.api_name}),
    url(r'^admin/components/report/$', 'gestion.administration.admin_views.component_report'),
    url(r'^admin/'                   , include(admin.site.urls                             )),
    url(r'^admin_tools/'             , include('admin_tools.urls'                          )),
    #This is specific to the debug server, another configuration is necessary for apache (and removing this of course)
    url(r'^media/(?P<path>.*)$'      , 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
)