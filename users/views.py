from django.shortcuts import redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from users.utils import role_required
from risks.models import RiskEvaluation
from django.db.models import Count
from datetime import timedelta
from django.utils import timezone



def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Ajusta según tus rutas
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')

@login_required
def redirect_dashboard(request):
    user = request.user
    if user.role == 'admin':
        return redirect('admin_dashboard')
    elif user.role == 'empleador':
        return redirect('empleador_dashboard')
    elif user.role == 'empleado':
        return redirect('empleado_dashboard')
    else:
        return redirect('login')  # fallback

def login_view(request):
    from django.contrib.auth.views import LoginView
    return LoginView.as_view(template_name='users/login.html')(request)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_empleado(request):
    return render(request, 'users/dashboard_empleado.html')

@login_required
def dashboard_empleador(request):
    return render(request, 'users/dashboard_empleador.html')

@login_required
def dashboard_admin(request):
    return render(request, 'users/dashboard_admin.html')

@login_required
@role_required(['admin', 'empleador'])
def actualizar_estado_riesgo(request, riesgo_id):
    riesgo = get_object_or_404(RiskEvaluation, id=riesgo_id)
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        if nuevo_estado in dict(RiskEvaluation.ESTADOS):
            riesgo.estado = nuevo_estado
            riesgo.save()
    return redirect('todos_riesgos')

@login_required
@role_required(['admin', 'empleador'])
def dashboard_admin(request):
    total_riesgos = RiskEvaluation.objects.count()

    riesgos_por_estado = RiskEvaluation.objects.values('estado').annotate(total=Count('id'))
    riesgos_por_factor = RiskEvaluation.objects.values('factor').annotate(total=Count('id'))

    ultimo_mes = timezone.now() - timedelta(days=30)
    riesgos_recientes = RiskEvaluation.objects.filter(fecha__gte=ultimo_mes).count()

    context = {
        'total': total_riesgos,
        'recientes': riesgos_recientes,
        'riesgos_estado': riesgos_por_estado,
        'riesgos_factor': riesgos_por_factor,
    }
    return render(request, 'users/dashboard_admin.html', context)