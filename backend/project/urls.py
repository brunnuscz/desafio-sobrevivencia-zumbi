from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('survivors/', include('api.routes.SurvivorRoutes')),
    path('items/', include('api.routes.ItemRoutes')),
    path('inventories/', include('api.routes.InventoryRoutes')),
    path('admin/', admin.site.urls),
]
