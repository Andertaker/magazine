from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^task_a/$', 'magazine.views.task_a', name='task_a'),
    url(r'^task_b/$', 'magazine.views.task_b', name='task_b'),
    url(r'^task_c/$', 'magazine.views.task_c', name='task_c'),

    url(r'^discounts/$', 'magazine.views.discounts'),


    url(r'^admin/', include(admin.site.urls)),
)
