__author__ = 'ryan'

from django.conf.urls import patterns, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('wexinbot.views',
                       url(r'^message/chat/', "reply"),
                       url(r'^message/send/', "send"),

                       url(r'^subscription/subscribe/', "subscribe"),
                       url(r'^subscription/subscribed/', "subscribed"),
                       url(r'^subscription/unsubscribe/', "unsubscribe"),
                       url(r'^subscription/unsubscribed/', "unsubscribed"),

                       url(r'^presence/available/', "available"),
                       url(r'^presence/unavailable/', "unavailable"),
                       url(r'^presence/probe/', "probe"),
)
