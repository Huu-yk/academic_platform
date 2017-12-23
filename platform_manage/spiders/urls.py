from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from spiders import views

urlpatterns = [
    url(r'^spiders/$', views.ConferenceList.as_view()),
    url(r'^spiders/(?P<pk>[0-9]+)/$', views.ConferenceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)