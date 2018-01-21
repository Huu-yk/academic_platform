from .models import ConferenceInfo
from .serializers import ConferenceSerilizer
from rest_framework import generics

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#使用泛类型视图
#get list and create
# class ConferenceList(generics.ListCreateAPIView):
#     queryset = ConferenceInfo.objects.all()
#     # if not queryset.exists():
#     #     try:
#     #         from .run import RunSpiders
#     #         queryset = ConferenceInfo.objects.all()
#     #     except ImportError as e:
#     #         print(e)
#     serializer_class = ConferenceSerilizer
#
# #update and delete
# class ConferenceDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ConferenceInfo.objects.all()
#     serializer_class = ConferenceSerilizer

#使用类基础视图
class ConferenceList(APIView):
    def get(self, request, format=None):
        conferences = ConferenceInfo.objects.all()
        serializer = ConferenceSerilizer(conferences, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ConferenceSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConferenceDetail(APIView):
    def get_object(self, pk):
        try:
            return ConferenceInfo.objects.get(pk=pk)
        except ConferenceInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ConferenceSerilizer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ConferenceSerilizer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)