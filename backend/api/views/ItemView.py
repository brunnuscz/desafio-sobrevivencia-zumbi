# import json
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view

# from api.models.ItemModel import ItemModel

# from api.serializers.ItemSerializer import ItemSerializer

from api.models.ItemModel import ItemModel
from api.serializers.ItemSerializer import ItemSerializer
from rest_framework import generics


class ItemList(generics.ListCreateAPIView):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer


"""
from rest_framework.viewsets import ModelViewSet
from api.serializers.ItemSerializer import ItemSerializer
from api.models.ItemModel import ItemModel

class ItemViewSet(ModelViewSet):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer
"""
    
"""
@api_view(['GET'])
def itemsList(request):
    items = ItemModel.objects.all()
    serializer = ItemSerializer(items, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def itemsCreate(request):
    item = ItemSerializer(data=request.data)
    if item.is_valid():
        item.save()
        return Response(item.data, status=status.HTTP_201_CREATED)

    return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)
"""