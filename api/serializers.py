from rest_framework import serializers
from api.models import usuarios
from api.models import restaurantes

class usuariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = usuarios
        fields = ['name', 'last_name', 'contactmail', 'cellphone']

class restaurantesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = restaurantes
        fields = ['name_restaurant', 'type_table', 'phone', 'address']
