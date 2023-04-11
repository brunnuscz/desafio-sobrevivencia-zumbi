from rest_framework import serializers
from api.models.InventoryModel import InventoryModel
from api.serializers.ItemSerializer import ItemSerializer
from api.serializers.SurvivorSerializer import SurvivorSerializer


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryModel
        exclude = ['id']

    def to_representation(self, instance):
        return {
            'item': ItemSerializer(instance.item).data,
            'amount': instance.amount
        }
 