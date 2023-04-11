from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.models.ItemModel import ItemModel
from api.serializers.ItemSerializer import ItemSerializer

# LISTAR TODOS OS ITENS
@api_view(['GET'])
def itemsList(request):
    itens = ItemModel.objects.all()
    serializer = ItemSerializer(itens, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# CRIAR UM ITEM
@api_view(['POST'])
def itemsCreate(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETAR UM ITEM
@api_view(['DELETE'])
def itemsDelete(request, pk):
    try:
        item = ItemModel.objects.get(id=pk)
        item.delete()
        return Response({'message': 'Item Deletado Com Sucesso'}, status=status.HTTP_200_OK)
    except ItemModel.DoesNotExist:
        return Response({'message': 'Item Não Encontrado'}, status=status.HTTP_404_NOT_FOUND)