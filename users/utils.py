from django.urls import path
from users import views
from django.shortcuts import redirect
from functools import wraps

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('redirect/', views.redirect_dashboard, name='redirect'),
    path('dashboard_admin/', views.dashboard, name='dashboard_admin'),
]

def role_required(roles_permitidos):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role in roles_permitidos:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('login')
        return _wrapped_view
    return decorator
