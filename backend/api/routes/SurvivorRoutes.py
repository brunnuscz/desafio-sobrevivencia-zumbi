from django.urls import path
from api.views import SurvivorView

urlpatterns = [
    path('', SurvivorView.survivorsList, name='survivors'),
]