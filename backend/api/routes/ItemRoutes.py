from django.urls import path
from api.views import ItemView


urlpatterns = [
    path('', ItemView.itemsList, name='items'),
    path('create/', ItemView.itemsCreate, name='items-create'),
    path('delete/<int:pk>/', ItemView.itemsDelete, name='items-delete'),
]
