from rest_framework import routers
from django.urls import path, include
from api.views import DeviceViewSet

router = routers.DefaultRouter()
router.register('devices', DeviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
