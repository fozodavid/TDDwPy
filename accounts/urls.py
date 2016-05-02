from django.conf.urls import patterns, url

import accounts.views

urlpatterns = [
    url(r'^login$', accounts.views.login, name='login'),
    url(r'^logout$', accounts.views.logout, name='logout'),
]
