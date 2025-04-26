from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ✅ Página de inicio personalizada
    path('', lambda request: render(request, 'inicio.html'), name='inicio'),

    # ✅ Panel administrativo de Django
    path('admin/', admin.site.urls),

    # ✅ Aplicaciones del proyecto
    path('usuarios/', include('users.urls')),
    path('riesgos/', include('risks.urls')),
    path('notificaciones/', include('notifications.urls')),

    # ✅ Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # ✅ Dashboard (redirige internamente según el rol)
    path('dashboard/', include('users.urls')),
]

# ✅ Para servir archivos de media (imagenes, etc.) en desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

