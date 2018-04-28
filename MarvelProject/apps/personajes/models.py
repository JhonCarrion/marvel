from django.db import models

# Create your models here.
HEROE = "HEROE"
VILLANO = "VILLANO"

TIPOS = (
    (HEROE, "HEROE"),
    (VILLANO, "VILLANO"),
)

class Personaje(models.Model):
    nombres = models.CharField(max_length=200)
    decripcion = models.TextField()
    #imagen = models.ImageField() #subir imagen
    imagen = models.URLField()
    tipo = models.CharField(max_length=20, choices=TIPOS, default=HEROE)
    fecha_creacion = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.nombres