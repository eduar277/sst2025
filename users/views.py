from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Bienvenido a la app de usuarios!")
