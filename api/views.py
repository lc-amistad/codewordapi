# Create your views here.
from rest_framework import viewsets
from api.models import usuarios
from .serializers import usuariosSerializer

class usuariosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = usuarios.objects.all()
    serializer_class = usuariosSerializer
    