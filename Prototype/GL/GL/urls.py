from settings              import MEDIA_URL
from django.contrib        import admin
from django.conf.urls      import patterns, include, url
from gestion.api.resources import resources_api

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$'                        , 'gestion.views.index'),
    url(r'^api/'                     , include(resources_api.urls)),
    url(r'^admin/products/report/$'  , 'gestion.administration.admin_views.product_chart_view'),
    url(r'^tastytools/'              , include('tastytools.urls'), {'api_name': resources_api.api_name}),
    url(r'^admin/components/report/$', 'gestion.administration.admin_views.component_report'),
    url(r'^admin/'                   , include(admin.site.urls                             )),
    url(r'^admin_tools/'             , include('admin_tools.urls'                          )),
    #This is specific to the debug server, another configuration is necessary for apache (and removing this of course)
    url(r'^media/(?P<path>.*)$'      , 'django.views.static.serve', {'document_root': MEDIA_ROOT, 'show_indexes':True}),
)