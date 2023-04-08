from django.urls import path
from api.views import InventoryView


urlpatterns = [
    path('', InventoryView.InventoryList.as_view()),
    path('<int:pk>/', InventoryView.InventoryDetail.as_view()),
]

"""
from django.urls import path
from api.views import InventoryView

urlpatterns = [
    path('', InventoryView.inventoriesList, name='inventories'),
    #path('survivor/<int:pk/>', InventoryView.inventoriesDetail, name='inventories-survivor'),
]
"""