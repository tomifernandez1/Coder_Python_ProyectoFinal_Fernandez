from django.db import models

# Create your models here.

class Mascotas(models.Model):
    nombre_mascota = models.CharField(max_length=30)
    codigo_mascota = models.IntegerField()
    email_dueño= models.EmailField()
    zona = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre Mascota: {self.nombre_mascota} - Codigo de Mascota: {self.codigo_mascota} - E-Mail: {self.email_dueño} -Zona:s {self.zona}"
    
class Cuidadores(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    zona = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail: {self.email} - Zona: {self.zona}"

class Reservas(models.Model):
    numero_reserva = models.IntegerField() 
    nombre_reserva= models.CharField(max_length=30)
    fecha_reserva = models.DateField()  
    confirmacion = models.BooleanField()
    def __str__(self):
        return f"Numero de Reserva: {self.numero_reserva} - Nombre de la Reserva: {self.nombre_reserva} - Fecha de la Reserva: {self.fecha_reserva} - Confirmacion {self.confirmacion}"

    