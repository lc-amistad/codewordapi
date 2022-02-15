# Create your views here.
from rest_framework import viewsets
from api.models import restaurantes, usuarios
from .serializers import restaurantesSerializer, usuariosSerializer

class usuariosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = usuarios.objects.all()
    serializer_class = usuariosSerializer
    
class restaurantesViewSet(viewsets.ModelViewSet):
        queryset = restaurantes.objects.all()
        serializer_class = restaurantesSerializer