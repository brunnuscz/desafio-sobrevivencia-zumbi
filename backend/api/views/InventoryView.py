from api.models.InventoryModel import InventoryModel
from api.serializers.InventorySerializer import InventorySerializer
from rest_framework import generics

class InventoryList(generics.ListCreateAPIView):
    queryset = InventoryModel.objects.all()
    serializer_class = InventorySerializer


class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryModel.objects.all()
    serializer_class = InventorySerializer




"""
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.models.InventoryModel import InventoryModel
from api.models.SurvivorModel import SurvivorModel
from api.serializers.InventorySerializer import InventorySerializer
from rest_framework.viewsets import ModelViewSet

class InventoryViewSet(ModelViewSet):
    queryset = InventoryModel.objects.all()
    serializer_class = InventorySerializer
    
    @api_view(['GET'])
    def inventoriesList(request):
        inventories = InventoryModel.objects.all()
        serializer = InventorySerializer(inventories, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

        #survivors = SurvivorModel.objects.filter(contaminated=False).values('id', 'name')
        #data = inventoriesSurvivor(survivors)

        #return Response({'inventories': data}, status=status.HTTP_200_OK)
    @api_view(['GET'])
    def inventoriesDetail(request, fk):
        survivor = SurvivorModel.objects.get(id=fk)
        if survivor.contaminated:
            return Response({'message': 'Sobrevivente infectado, impossível acessar/manipular inventário'}, status=status.HTTP_403_FORBIDDEN)
        else:
            inventories = InventoryModel.objects.filter(survivor=fk)
            serializer = InventorySerializer(inventories, many=True)

            return Response({'survivorId': fk, 'survivor': survivor.name, 'items': serializer.data}, status=status.HTTP_200_OK)
    

    def inventoriesSurvivor(survivors):
        data = []

        for s in survivors:
            inventories = InventoryModel.objects.filter(survivors = s['id'])
            serializer = InventorySerializer(inventories, many=True)
            data.append(
                {
                    'survivorId': s['id'],
                    'survivor': s['name'],
                    'items': serializer.data
                }
            )

        return data
"""