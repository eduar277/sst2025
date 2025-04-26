from notifications.models import Notification

def notificaciones_context(request):
    if request.user.is_authenticated:
        nuevas_notificaciones = Notification.objects.filter(usuario=request.user, leida=False).count()
    else:
        nuevas_notificaciones = 0

    return {
        'nuevas_notificaciones': nuevas_notificaciones
    }

