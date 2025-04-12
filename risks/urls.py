from django.urls import path
from . import views

urlpatterns = [
    path('evaluar/', views.evaluar_riesgo, name='evaluar_riesgo'),
    path('mis/', views.mis_riesgos, name='mis_riesgos'),
    path('todos/', views.listar_todos_los_riesgos, name='todos_riesgos'),
    path('exportar/pdf/', views.exportar_riesgos_pdf, name='exportar_riesgos_pdf'),



]
