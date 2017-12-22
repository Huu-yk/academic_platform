from spiders.models import ConferenceInfo
from spiders.serializers import ConferenceSerilizer
from rest_framework import generics

#使用泛类型视图
#get list and create
class ConferenceList(generics.ListCreateAPIView):
    queryset = ConferenceInfo.objects.all()
    if not queryset.exists():
        try:
            from .run import RunSpiders
            queryset = ConferenceInfo.objects.all()
        except ImportError as e:
            print(e)
    serializer_class = ConferenceSerilizer

#update and delete
class ConferenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConferenceInfo.objects.all()
    serializer_class = ConferenceSerilizer


