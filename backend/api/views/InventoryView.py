from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.models.InventoryModel import InventoryModel
from api.models.SurvivorModel import SurvivorModel
from api.serializers.InventorySerializer import InventorySerializer

# LISTAR OS INVENTÁRIOS
@api_view(['GET'])
def inventoriesList(request):
    try:
        survivors = SurvivorModel.objects.filter(contaminated=False).values('id', 'name')
        data = inventoriesSurvivor(survivors)
        return Response({'inventories': data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': e}, status=status.HTTP_400_BAD_REQUEST)

# LOOP MOSTRAR DADOS
def inventoriesSurvivor(survivors):
    data = []
    for s in survivors:
        inventaries = InventoryModel.objects.filter(survivor=s['id'])
        serializer = InventorySerializer(inventaries, many=True)
        data.append({
            'survivorId': s['id'],
            'survivor': s['name'],
            'items': serializer.data
        })
    return data