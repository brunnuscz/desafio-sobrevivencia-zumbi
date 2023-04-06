from rest_framework import serializers
from api.models.InventoryModel import InventoryModel
from api.serializers.ItemSerializer import ItemSerializer

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryModel
        exclude = ['id']

    def showData(self, instance):
        return {
            'item': ItemSerializer(instance.item).data,
            'amount': instance.amount
        }