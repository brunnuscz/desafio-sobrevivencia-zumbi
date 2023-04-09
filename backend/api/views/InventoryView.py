from api.models.InventoryModel import InventoryModel
from api.serializers.InventorySerializer import InventorySerializer
from rest_framework import generics

class InventoryList(generics.ListCreateAPIView):
    queryset = InventoryModel.objects.all()
    serializer_class = InventorySerializer


class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryModel.objects.all()
    serializer_class = InventorySerializer
