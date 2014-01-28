from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pypnrstatus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'pypnrstatus.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
