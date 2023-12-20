from django.db import models


class Bolo(models.Model):
    titulo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    foto = models.ImageField(upload_to="bolos", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Bolo"
        verbose_name_plural = "Bolos"
