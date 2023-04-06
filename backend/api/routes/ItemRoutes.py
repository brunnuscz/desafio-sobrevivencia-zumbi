from django.urls import path
from api.views import ItemView

urlpatterns = [
    path('list/', ItemView.itemsList, name='items'),
    path('create/', ItemView.itemsCreate, name='items-create'),
]
    
