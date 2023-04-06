from django.db import models
from .SurvivorModel import SurvivorModel # tá tudo na mesma pasta
from .ItemModel import ItemModel


class InventoryModel(models.Model):
    class Meta:
        db_table = 'inventories'
    
    survivor = models.ForeignKey(SurvivorModel, on_delete=models.CASCADE) # chave estrangeira
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    amount = models.IntegerField()
