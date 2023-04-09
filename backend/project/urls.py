from django.contrib import admin
from django.urls import path, include
from api.routes import InventoryRoutes, ItemRoutes, SurvivorRoutes

urlpatterns = [
    path('survivors/', include(SurvivorRoutes)),
    path('items/', include(ItemRoutes)),
    path('inventories/', include(InventoryRoutes)),
    path('admin/', admin.site.urls),
]
