from rest_framework.serializers import ModelSerializer
from api.models.ItemModel import ItemModel

class ItemSerializer(ModelSerializer):
    class Meta:
        model = ItemModel
        fields = ['id', 'name', 'point']