from django.urls import path
from api.views import ItemView


urlpatterns = [
    path('', ItemView.ItemList.as_view()),
    path('<int:pk>/', ItemView.ItemDetail.as_view()),
]


"""
from django.urls import path
from api.views import ItemView

urlpatterns = [
    path('', ItemView.itemsList, name='items'),
    path('create/', ItemView.itemsCreate, name='items-create'),
]
"""   
