from django.db import models

# Create your models here.

class Credit(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    dni = models.IntegerField(blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)

    productos = models.JSONField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.nombre