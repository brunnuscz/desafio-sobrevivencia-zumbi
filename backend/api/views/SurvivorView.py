import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.models.SurvivorModel import SurvivorModel
from api.models.ItemModel import ItemModel
from api.serializers.SurvivorSerializer import SurvivorSerializer
from api.serializers.InventorySerializer import InventorySerializer

# LISTAR TODOS OS SOBREVIVENTES
@api_view(['GET'])
def survivorsList(request):
    survivors = SurvivorModel.objects.all()
    serializer = SurvivorSerializer(survivors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# EXIBIR UM SOBREVIVENTE EM ESPECIFICO
@api_view(['GET'])
def survivorsDetail(request, pk):
    try:
        survivors = SurvivorModel.objects.get(id=pk)
        serializer = SurvivorSerializer(survivors, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except SurvivorModel.DoesNotExist:
        return Response({'message': 'Sobrevivente não encontrado'}, status=status.HTTP_404_NOT_FOUND)

# CADASTRAR UM SOBREVIVENTE
@api_view(['POST'])
def survivorsCreate(request):
    try:
        if request.data.get('inventory') == None or len(request.data.get('inventory')) == 0:
            return Response({'message': 'É necessário declarar os itens do inventário'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            inventory = request.data.get('inventory')
            serializer = SurvivorSerializer(data=request.data)
            if serializer.is_valid():
                s = serializer.save()
                for i in inventory:
                    serializerI = InventorySerializer(data={
                        "survivor": s.id,
                        "item": i.get('id'),
                        "amount": i.get('amount')
                    })
                    if serializerI.is_valid():
                        serializerI.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ItemModel.DoesNotExist:
        return Response({'message': 'Item declarado não exite no sistema'}, status=status.HTTP_400_BAD_REQUEST)

# ATUALIZAR LOCALIZAÇÃO DO SOBREVIVENTE
@api_view(['PUT'])
def survivorLocalization(request, pk):
    try:
        data = request.data
        survivor = SurvivorModel.objects.get(id=pk)
        if data.get('latitude') == None or data.get('longitude') == None:
            return Response({'message': 'Campo de localização faltando'}, status=status.HTTP_400_BAD_REQUEST)
        survivor.latitude = data.get('latitude')
        survivor.longitude = data.get('longitude')
        survivor.save(update_fields=['latitude', 'longitude'])
        return Response({'message': 'Localização Atualizada com Sucesso'}, status=status.HTTP_200_OK)
    except SurvivorModel.DoesNotExist:
        return Response({'message': 'Sobrevivente Não Encontrado'}, status=status.HTTP_404_NOT_FOUND)

# DELETAR SOBREVIVENTE
@api_view(['DELETE'])
def survivorsDelete(request, pk):
    try:
        survivor = SurvivorModel.objects.get(id=pk)
        survivor.delete()
        return Response({'message': 'Sobrevivente Deletado com Sucesso'}, status=status.HTTP_200_OK)
    except SurvivorModel.DoesNotExist:
        return Response({'message': 'Sobrevivente Não Encontrado'}, status=status.HTTP_404_NOT_FOUND)

