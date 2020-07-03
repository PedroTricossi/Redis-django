from django.contrib import admin
from django.urls import path, include
from store.routers import router as store_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(store_router.urls)),
]
