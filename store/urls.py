from django.urls import path
from .views import view_products, view_cached_products

urlpatterns = [
    path('cache/', view_cached_products),
]