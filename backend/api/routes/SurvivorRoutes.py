from django.urls import path
from api.views import SurvivorView


urlpatterns = [
    path('', SurvivorView.SurvivorList.as_view()),
    path('<int:pk>/', SurvivorView.SurvivorDetail.as_view()),
]
