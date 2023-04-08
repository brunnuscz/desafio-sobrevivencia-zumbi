from django.contrib import admin

from .models.SurvivorModel import SurvivorModel
from .models.InventoryModel import InventoryModel
from .models.ItemModel import ItemModel


admin.site.register(SurvivorModel)
admin.site.register(InventoryModel)
admin.site.register(ItemModel)