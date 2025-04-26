from django.urls import path
from users import views

urlpatterns = [
    # Autenticación
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),  # 🔥 Correcto

    # Redireccionamiento
    path('redirect/', views.redirect_dashboard, name='redirect'),

    # Dashboard del administrador o empleador
    path('dashboard_admin/', views.dashboard, name='dashboard_admin'),
]


