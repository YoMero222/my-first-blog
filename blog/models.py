from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    descripcion = models.TextField(default="")
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    imagen=models.ImageField( default="")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


    def tipo(self):

        return "Post"

class Integrantes(models.Model):
    nombre=models.CharField(max_length=200,default="")
    puesto=models.CharField(max_length=200,default="")
    correo=models.EmailField(max_length=200,default="")
    facebook=models.CharField(max_length=200,default="")
    twitter=models.CharField(max_length=200,default="")
    instagram=models.CharField(max_length=200,default="")
    imagenDePerfil=models.ImageField( default="")

    def __str__(self):
        return self.nombre



class Galeria(models.Model):
    nombre=models.CharField(max_length=200,default="")
    imagen = models.ImageField()

    def __str__(self):
        return self.nombre

    def tipo(self):
        
        return "Galeria"

def upload_t(instance, filename):
    return 'galeria/%s/%s' % (instance.galeria.nombre, filename)



class ImagenEnGaleria(models.Model):
    galeria = models.ForeignKey('Galeria', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to=upload_t)

    def __str__(self):
        return self.imagen.name
