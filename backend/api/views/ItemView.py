from api.models.ItemModel import ItemModel
from api.serializers.ItemSerializer import ItemSerializer
from rest_framework import generics


class ItemList(generics.ListCreateAPIView):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer
