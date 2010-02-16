# -*- coding: utf-8 -*-

import datetime
from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('',
    url(r'^editor/$',       'ray.views.ray_editor',     name='ray-editor'),
    url(r'^browse/$',       'ray.views.ray_browse',     name='ray-browse'),
    url(r'^open/$',         'ray.views.ray_open',       name='ray-open'),
    url(r'^fileinfos/$',    'ray.views.ray_fileinfos',  name='ray-fileinfos'),
    url(r'^svn/log/$',      'ray.views.ray_svn_log',    name='ray-svn-log'),
) 
