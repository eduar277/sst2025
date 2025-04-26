from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Notification
from django.shortcuts import get_object_or_404
from django.contrib import messages

@login_required
def lista_notificaciones(request):
    notificaciones = Notification.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'notifications/lista_notificaciones.html', {'notificaciones': notificaciones})


@login_required
def marcar_notificacion_leida(request, notificacion_id):
    notificacion = get_object_or_404(Notification, id=notificacion_id, usuario=request.user)
    if request.method == 'POST':
        notificacion.leida = True
        notificacion.save()
        messages.success(request, "Notificación marcada como leída.")
    return redirect('lista_notificaciones')