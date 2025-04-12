from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('empleado', 'Empleado'),
        ('empleador', 'Empleador'),
    )
    role = models.CharField(max_length=20, choices=ROLES)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

