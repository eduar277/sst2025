from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.register_user, name='register_user'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('redirect/', views.redirect_dashboard, name='redirect_dashboard'),
    path('empleado/dashboard/', views.dashboard_empleado, name='empleado_dashboard'),
    path('empleador/dashboard/', views.dashboard_empleador, name='empleador_dashboard'),
    path('admin/dashboard/', views.dashboard_admin, name='admin_dashboard'),
    path('riesgo/<int:riesgo_id>/estado/', views.actualizar_estado_riesgo, name='actualizar_estado_riesgo'),
    path('dashboard_admin/', views.dashboard_admin, name='dashboard_admin'),


]


