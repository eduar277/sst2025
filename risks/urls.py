from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.listar_todos_los_riesgos, name='todos_riesgos'),
    path('evaluar/', views.evaluar_riesgo, name='evaluar_riesgo'),
    path('mis/', views.mis_riesgos, name='mis_riesgos'),
    path('actualizar_estado/<int:riesgo_id>/', views.actualizar_estado_riesgo, name='actualizar_estado_riesgo'),  # 🔥 Línea que faltaba
    path('exportar/pdf/', views.exportar_riesgos_pdf, name='exportar_riesgos_pdf'),
    path('exportar/excel/', views.exportar_riesgos_excel, name='exportar_riesgos_excel'),
]
