from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                        url(r'^_ah/xmpp/', include('wexinbot.urls')),
                        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^$', 'wexinbot.views.home'),
)
