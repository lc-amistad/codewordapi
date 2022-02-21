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
        fields = ['name_restaurant', 'type_table_1', 'type_table_2','type_table_3','name_menu','saucer_1',
                     'saucer_2', 'saucer_3', 'phone', 'address','restaurant_image']
