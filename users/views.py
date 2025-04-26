from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from risks.models import RiskEvaluation
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta


# ✅ Vista de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('redirect')
        else:
            return render(request, 'users/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'users/login.html')


# ✅ Vista de logout
def logout_view(request):
    logout(request)
    return redirect('login')


# ✅ Vista de registro
def registro_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('redirect')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/registro.html', {'form': form})


# ✅ Redireccionar según rol
@login_required
def redirect_dashboard(request):
    if request.user.role == 'admin' or request.user.role == 'empleador':
        return redirect('dashboard_admin')
    elif request.user.role == 'empleado':
        return redirect('mis_riesgos')
    else:
        return redirect('login')


# ✅ Dashboard Admin
@login_required
def dashboard(request):
    total = RiskEvaluation.objects.count()
    riesgos_estado = RiskEvaluation.objects.values('estado').annotate(total=Count('id'))
    riesgos_factor = RiskEvaluation.objects.values('factor').annotate(total=Count('id'))
    recientes = RiskEvaluation.objects.filter(fecha__gte=timezone.now() - timedelta(days=30)).count()

    context = {
        'total': total,
        'riesgos_estado': riesgos_estado,
        'riesgos_factor': riesgos_factor,
        'recientes': recientes,
    }
    return render(request, 'users/dashboard_admin.html', context)
