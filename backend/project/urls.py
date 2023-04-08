from django.contrib import admin
from django.urls import path, include
from api.routes import InventoryRoutes, ItemRoutes, SurvivorRoutes

urlpatterns = [
    path('survivors/', include(SurvivorRoutes)),
    path('items/', include(ItemRoutes)),
    path('inventories/', include(InventoryRoutes)),
    path('admin/', admin.site.urls),
]


"""
from rest_framework import routers
from api.views.ItemView import ItemViewSet
from api.views.InventoryView import InventoryViewSet
from api.views.SurvivorView import SurvivorViewSet
from django.urls import path, include
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet, basename='Item')
router.register(r'survivors', SurvivorViewSet, basename='Survivor')
router.register(r'inventories', InventoryViewSet, basename='Inventory')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
"""
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('survivors/', include('api.routes.SurvivorRoutes')),
    path('items/', include('api.routes.ItemRoutes')),
    path('inventories/', include('api.routes.InventoryRoutes')),
    path('admin/', admin.site.urls),
]
"""