from django.urls import path
from api.views import SurvivorView


urlpatterns = [
    path('', SurvivorView.survivorsList, name='survivors'),
    path('detail/<int:pk>/', SurvivorView.survivorsDetail, name='survivor-detail'),
    path('create/', SurvivorView.survivorsCreate, name='survivor-create'),
    path('delete/<int:pk>/', SurvivorView.survivorsDelete, name='survivor-delete'),
    path('update/<str:pk>/', SurvivorView.survivorLocalization, name='survivor-localization'),
]
