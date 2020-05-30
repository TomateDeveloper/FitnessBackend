from django.conf.urls import url
from groups.views import create_group, list_groups, get_group, update_group, delete_group

urlpatterns = [
    url(r'^get/(?P<groups_id>\w{0,50})/$', get_group),
    url(r'^list/$', list_groups),
    url(r'^create/$', create_group),
    url(r'^update/(?P<groups_id>\w{0,50})/$', update_group),
    url(r'^delete/(?P<groups_id>\w{0,50})/$', delete_group)
]
