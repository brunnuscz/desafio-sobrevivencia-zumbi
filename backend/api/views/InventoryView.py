from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.models.InventoryModel import InventoryModel
from api.models.SurvivorModel import SurvivorModel
from api.serializers.InventorySerializer import InventorySerializer

@api_view(['GET'])
def inventoriesList(request):
    survivor = SurvivorModel.objects.filter(contaminated=False).values('id', 'name')
    data = inventoriesSurvivor(survivor)

    return Response({'inventoies': data}, status=status.HTTP_200_OK)
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
                'survivor': s['nome'],
                'items': serializer.data
            }
        )

    return data
