from rest_framework import routers

from .viewsets import ProductViewSet


router = routers.DefaultRouter()
router.register('api', ProductViewSet)