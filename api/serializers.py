from rest_framework import serializers
from api.models import usuarios
from api.models import restaurantes
from api.models import menu
from api.models import promociones
from api.models import booking

class usuariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = usuarios
        fields = ['name', 'last_name', 'contactmail', 'cellphone']

class menuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = menu
        fields = ['nombre_platillo', 'ingredientes']

class promocionesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = promociones
        fields = ['nombre_promocion', 'descripcion']

class bookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = booking
        fields = ['nombre_usuario', 'apellido_usuario', 'telefono', 'email', 'dia_hora_booking', 'solicitud_especial']

class restaurantesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = restaurantes
        fields = ['name_restaurant', 'type_table_1', 'type_table_2','type_table_3','name_menu','saucer_1',
                     'saucer_2', 'saucer_3', 'phone', 'address','restaurant_image']
