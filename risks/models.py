from django.db import models
from django.conf import settings


class RiskEvaluation(models.Model):
    FACTORES = [
        ('iluminacion', 'Iluminación'),
        ('ergonomia', 'Ergonomía'),
        ('pausas', 'Pausas activas'),
        ('ruido', 'Ruido'),
        ('otros', 'Otros'),
    ]

    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('revision', 'En revisión'),
        ('mitigado', 'Mitigado'),
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    factor = models.CharField(max_length=50, choices=FACTORES)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    imagen = models.ImageField(upload_to='riesgos/', blank=True, null=True)  # ✅ Imagen opcional

    def __str__(self):
        return f"{self.usuario.username} - {self.get_factor_display()} - {self.fecha.strftime('%Y-%m-%d')}"

