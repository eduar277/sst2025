from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notificaciones, name='lista_notificaciones'),  # ✅ correcto
    path('marcar/<int:notificacion_id>/', views.marcar_notificacion_leida, name='marcar_notificacion_leida'),
]
