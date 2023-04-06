# import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from api.models.SurvivorModel import SurvivorModel
#from api.models.ItemModel import ItemModel
#from api.models.InventoryModel import InventoryModel

from api.serializers.SurvivorSerializer import SurvivorSerializer
#from api.serializers.ItemSerializer import ItemSerializer
#from api.serializers.InventorySerializer import InventorySerializer


# LISTAR TODOS OS SOBREVIVENTES CADASTRADOS
@api_view(['GET'])
def survivorsList(request):
    survivors = SurvivorModel.objects.all()
    serializer = SurvivorSerializer(survivors, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

# CADASTRAR UM NOVO SOBREVIVENTE AO BANCO DE DADOS

@api_view(['POST'])
def survivorsCreate(request):
    survivor = SurvivorSerializer(data=request.data)
    if survivor.is_valid():
        survivor.save()
        return Response(survivor.data, status=status.HTTP_201_CREATED)

    return Response(survivor.errors, status=status.HTTP_400_BAD_REQUEST)
    """
    # se não tiver nenhum inventário ou se for igual a zero
    if (request.data.get('inventory') == None) or (len(request.data.get('inventory')) == 0):
        return Response({
            'message': 'É preciso que os itens do inventário sejam declarados'
        }, status = status.HTTP_400_BAD_REQUEST)
    else:
        inventory = request.data.get('inventory')

        for i in inventory:
            item = ItemModel.objects.get(pk=i.get('id'))
            print(item)

            survivor = SurvivorSerializer(data=request.data)
            if survivor.is_valid(): # se for valido
                warrior = survivor.save()
                # pegar os items passado e colocar
                for i in inventory:
                    serializerI = InventorySerializer(
                        data={
                            "survivor": warrior.id,
                            "item": i.get('id'),
                            "quantidade": i.get('quantidade')
                        }
                    )

                    if serializerI.is_valid():
                        serializerI.save()
            
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ItemModel.DoesNotExist:
        return Response({'message': 'Item declarado não exite no sistema'}, status=status.HTTP_400_BAD_REQUEST)
  """