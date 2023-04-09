from rest_framework import generics
from api.models.SurvivorModel import SurvivorModel
from api.serializers.SurvivorSerializer import SurvivorSerializer


class SurvivorList(generics.ListCreateAPIView):
    queryset = SurvivorModel.objects.all()
    serializer_class = SurvivorSerializer


class SurvivorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SurvivorModel.objects.all()
    serializer_class = SurvivorSerializer
