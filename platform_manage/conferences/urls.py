from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^conferences/$', views.ConferenceList.as_view()),
    url(r'^conferences/(?P<pk>[0-9]+)/$', views.ConferenceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)