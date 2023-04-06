from django.urls import path
from api.views import SurvivorView


urlpatterns = [
    path('list/', SurvivorView.survivorsList, name='survivors'),
    path('create/', SurvivorView.survivorsCreate, name='survivors-create'),
]