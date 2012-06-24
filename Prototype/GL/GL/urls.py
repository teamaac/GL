from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/products/report/$'  , 'gestion.administration.admin_views.product_report'  ),
	url(r'^admin/components/report/$', 'gestion.administration.admin_views.component_report'),
	url(r'^admin/'                   , include(admin.site.urls                             )),
	url(r'^admin_tools/'             , include('admin_tools.urls'                          )),
)
