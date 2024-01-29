from user.models import Homiy
from user.api.serializers import LegalEntityHomiySerializer, HomiySerializer
from rest_framework import generics


class LegalHomiyCreationView(generics.ListCreateAPIView):
    queryset = Homiy.objects.filter(role=1)
    serializer_class = LegalEntityHomiySerializer


class HomiyCreationView(generics.ListCreateAPIView):
    queryset = Homiy.objects.filter(role=0)
    serializer_class = HomiySerializer


# class UserAuthenticationView(generics.)