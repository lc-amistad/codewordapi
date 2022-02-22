# Create your views here.
from rest_framework import viewsets
from api.models import restaurantes, usuarios, menu, promociones, booking
from .serializers import menuSerializer, restaurantesSerializer, usuariosSerializer, promocionesSerializer, bookingSerializer

class usuariosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = usuarios.objects.all()
    serializer_class = usuariosSerializer
    
class restaurantesViewSet(viewsets.ModelViewSet):
        queryset = restaurantes.objects.all()
        serializer_class = restaurantesSerializer

class menuViewSet(viewsets.ModelViewSet):
        queryset = menu.objects.all()
        serializer_class = menuSerializer

class promocionesViewSet(viewsets.ModelViewSet):
        queryset = promociones.objects.all()
        serializer_class = promocionesSerializer

class bookingViewSet(viewsets.ModelViewSet):
        queryset = booking.objects.all()
        serializer_class = bookingSerializer