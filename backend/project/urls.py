from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('survivors/', include('api.routes.SurvivorRoutes')),
    path('admin/', admin.site.urls),
]
