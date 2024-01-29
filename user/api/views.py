from user.models import Homiy, Student
from user.api.serializers import (LegalEntityHomiySerializer, HomiyPOSTSerializer, HomiylarGETSerializer,
                                  HomiyUpdateSerializer, HomiyGETSerializer, TalabalarListCreateSerializer)
from rest_framework import generics, status
from rest_framework.response import Response


class LegalHomiyCreationView(generics.CreateAPIView):
    queryset = Homiy.objects.filter(role=1)
    serializer_class = LegalEntityHomiySerializer


class HomiyCreationView(generics.CreateAPIView):
    queryset = Homiy.objects.filter(role=0)
    serializer_class = HomiyPOSTSerializer


class HomiylarView(generics.ListAPIView):
    queryset = Homiy.objects.all()
    serializer_class = HomiylarGETSerializer

    def get_queryset(self):
        queryset = Homiy.objects.all()

        # Filter by date
        date_param = self.request.query_params.get('date_joined', None)
        if date_param:
            queryset = queryset.filter(date_joined__date=date_param)

        # Filter by holat (status)
        holat_param = self.request.query_params.get('holat', None)
        if holat_param:
            queryset = queryset.filter(holat=holat_param)

        # Filter by tolov_summasi (payment amount)
        tolov_summasi_param = self.request.query_params.get('tolov_summasi', None)
        if tolov_summasi_param:
            queryset = queryset.filter(tolov_summasi=tolov_summasi_param)

        return queryset


class HomiySingleRetrieveView(generics.RetrieveAPIView):
    serializer_class = HomiyGETSerializer

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        query = Homiy.objects.get(id=pk)
        serializer = self.get_serializer(query)
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)


class HomiyRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = HomiyUpdateSerializer
    queryset = Homiy.objects.all()

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        query = Homiy.objects.get(id=pk)
        serializer = self.get_serializer(query)
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)


class TalabaListCreateView(generics.ListCreateAPIView):
    serializer_class = TalabalarListCreateSerializer
    queryset = Student.objects.all()

