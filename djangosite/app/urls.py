# /usr/env python
#_*_coding:utf-8_*_

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'moments_input',views.moments_input),
    url(r'',views.welcome),
]


