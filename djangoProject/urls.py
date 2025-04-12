from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('admin/', admin.site.urls),
    path('usuarios/', include('users.urls')),  # Esto conecta users/urls.py
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('riesgos/', include('risks.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)