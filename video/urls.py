from django.conf.urls import url
from video.views import create_video, list_videos, get_video, update_video, delete_video

urlpatterns = [
    url(r'^get/(?P<video_id>\w+)/$', get_video),
    url(r'^list/$', list_videos),
    url(r'^create/$', create_video),
    url(r'^update/(?P<video_id>\w{0,50})/$', update_video),
    url(r'^delete/(?P<video_id>\w{0,50})/$', delete_video)
]
