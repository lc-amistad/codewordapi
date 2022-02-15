
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

from api import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.usuariosViewSet)
router.register(r'restaurantes', views.restaurantesViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
