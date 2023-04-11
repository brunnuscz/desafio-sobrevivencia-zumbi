import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.models.SurvivorModel import SurvivorModel
from api.models.ItemModel import ItemModel
from api.serializers.SurvivorSerializer import SurvivorSerializer
from api.serializers.InventorySerializer import InventorySerializer

@api_view(['GET'])
def survivorsList(request):
    survivors = SurvivorModel.objects.all()
    serializer = SurvivorSerializer(survivors, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def survivorsDetail(request, pk):
    try:
        survivors = SurvivorModel.objects.get(id=pk)
        serializer = SurvivorSerializer(survivors, many=False)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    except SurvivorModel.DoesNotExist:
        return Response({'message': 'Sobrevivente não encontrado'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def survivorsCreate(request):

    try:
        if request.data.get('inventory') == None or len(request.data.get('inventory')) == 0:
            return Response({'message': 'É necessário declarar os itens do inventário'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            inventory = request.data.get('inventory')

            for i in inventory:
                item = ItemModel.objects.get(pk=i.get('id'))

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

@api_view(['DELETE'])
def survivorsDelete(request, pk):
    try:
        survivor = SurvivorModel.objects.get(id=pk)
        survivor.delete()
        return Response({'message': 'Sobrevivente Deletado com Sucesso'}, status=status.HTTP_200_OK)
    except SurvivorModel.DoesNotExist:
        return Response({'message': 'Sobrevivente Não Encontrado'}, status=status.HTTP_404_NOT_FOUND)

