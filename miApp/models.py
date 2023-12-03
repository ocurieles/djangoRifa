from django.db import models


class Rifas(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    descripcion = models.TextField()
    numeros_disponibles = models.PositiveIntegerField()
    numeros_vendidos = models.PositiveIntegerField()
    estado = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='imagenes')


class Premios(models.Model):
    rifas=models.ForeignKey(Rifas,on_delete=models.CASCADE)
    nombre = models.CharField (max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='premio_imagenes')


class Venta(models.Model):
    rifas = models.ForeignKey(Rifas,related_name='rifas',on_delete=models.CASCADE)
    nombre=models.CharField(max_length=100)
    email=models.CharField(max_length=100,blank= True)
    telefono=models.IntegerField()
    numero_compra=models.IntegerField()
    codigo=models.CharField(max_length=100)
    sorteado = models.BooleanField(default=False)


class Participante(models.Model):
    nombre = models.CharField(max_length=50,unique=True)
    email = models.CharField(max_length=50, unique=True )
    winner  = models.BooleanField(default = False )
    numero_sorteo = models.IntegerField(default=0)  