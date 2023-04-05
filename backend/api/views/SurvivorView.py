# import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from api.models.SurvivorModel import SurvivorModel

from api.serializers.SurvivorSerializer import SurvivorSerializer

@api_view(['GET'])
def survivorsList(request):
    survivors = SurvivorModel.objects.all()
    serializer = SurvivorSerializer(survivors, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)
