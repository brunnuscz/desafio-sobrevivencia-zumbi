from rest_framework.serializers import ModelSerializer
from api.models.SurvivorModel import SurvivorModel

class SurvivorSerializer(ModelSerializer):
    class Meta:
        model = SurvivorModel
        fields = ['id', 'name', 'age', 'sex', 'latitude', 'longitude', 'contaminated', 'reports']