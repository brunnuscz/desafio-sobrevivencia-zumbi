from django.urls import path
from api.views import InventoryView


urlpatterns = [
    path('', InventoryView.inventoriesList, name='inventories'),
]
