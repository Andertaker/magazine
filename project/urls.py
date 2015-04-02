from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
     url(r'^task_a/$', 'magazine.views.task_a', name='task_a'),


    url(r'^admin/', include(admin.site.urls)),
)
