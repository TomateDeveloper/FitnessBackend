from django.conf.urls import url
from categories.views import create_category, list_categories, get_category, update_category, delete_category

urlpatterns = [
    url(r'^get/(?P<category_id>\w{0,50})/$', get_category),
    url(r'^list/$', list_categories),
    url(r'^create/$', create_category),
    url(r'^update/(?P<category_id>\w{0,50})/$', update_category),
    url(r'^delete/(?P<category_id>\w{0,50})/$', delete_category)
]
