from django.conf.urls import url
from .views import CreateUserAPIView, UserRetrieveUpdateAPIView, authenticate_user

urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'^obtain_token/$', authenticate_user),
    url(r'^update/$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^get/$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^get/(?P<id>\w+)$', UserRetrieveUpdateAPIView.as_view()),
]
