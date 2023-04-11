from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.models.InventoryModel import InventoryModel
from api.models.SurvivorModel import SurvivorModel
from api.serializers.InventorySerializer import InventorySerializer

@api_view(['GET'])
def inventariosList(request):
    try:
        survivors = SurvivorModel.objects.filter(contaminated=False).values('id', 'name')
        data = inventariesSurvivor(survivors)
        return Response({'inventories': data}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'message': e}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def inventoriesDetail(request, fk):
    try:
        survivor = SurvivorModel.objects.get(id=fk)
        if survivor.contaminated:
            return Response({'message': 'Não é possível acessar inventário, sobrevivente infectado'}, status=status.HTTP_403_FORBIDDEN)
        else:
            inventaries = InventoryModel.objects.filter(survivor=fk)
            serializer = InventorySerializer(inventaries, many=True)

            return Response({'survivorId': fk, 'survivor': survivor.name, 'itens': serializer.data}, status=status.HTTP_200_OK)
    except SurvivorModel.DoesNotExist:
        return Response({'message': 'Sobrevivente não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    
def inventariesSurvivor(survivors):
    data = []

    for s in survivors:
        inventaries = InventoryModel.objects.filter(survivor=s['id'])
        serializer = InventorySerializer(inventaries, many=True)

        data.append(
            {
                'survivorId': s['id'],
                'survivor': s['name'],
                'items': serializer.data
            }
        )

    return data