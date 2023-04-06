from django.urls import path
from api.views import InventoryView

urlpatterns = [
    path('list/', InventoryView.inventoriesList, name='inventories'),
    #path('survivor/<int:pk/>', InventoryView.inventoriesDetail, name='inventories-survivor'),
]