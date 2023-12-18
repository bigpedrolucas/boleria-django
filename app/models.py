from django.db import models


class Bolo(models.Model):
    titulo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=3, decimal_places=2)
    foto = models.ImageField(upload_to="bolos_fotos/", null=True)

    def __str__(self):
        return self.titulo
