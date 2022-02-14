from rest_framework import serializers
from api.models import usuarios


class usuariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = usuarios
        fields = ['name', 'last_name', 'contactmail', 'cellphone']
