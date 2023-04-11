from django.urls import path
from api.views import InventoryView


urlpatterns = [
    path('', InventoryView.inventariosList, name='inventories'),
    path('survivors/<int:pk>/', InventoryView.inventoriesDetail, name='inventories-survivor'),
]
