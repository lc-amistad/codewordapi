from django.db import models

# Create your models here.

class usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    # id = models.AutoField(primary_key=True, **opciones) 
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contactmail = models.CharField(max_length=30)
    cellphone = models.PositiveIntegerField()

class menu(models.Model):
    nombre_platillo = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=50)

class promociones(models.Model):
    nombre_promocion = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

class booking(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    telefono = models.PositiveIntegerField()
    email = models.CharField(max_length=30)
    dia_hora_booking = models.DateTimeField()
    solicitud_especial = models.CharField(max_length=50)

class restaurantes(models.Model):
    name_restaurant = models.CharField(max_length=50)
    type_table_1 = models.CharField(max_length=50)
    type_table_2 = models.CharField(max_length=50)
    type_table_3 = models.CharField(max_length=50)
    name_menu = models.CharField(max_length=50)
    saucer_1 = models.CharField(max_length=50)
    saucer_2 = models.CharField(max_length=50)
    saucer_3 = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=30)
    restaurant_image = models.ImageField('view',blank=True,upload_to="media")