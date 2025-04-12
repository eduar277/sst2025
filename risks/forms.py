from django import forms
from .models import RiskEvaluation
from users.models import CustomUser

class RiskEvaluationForm(forms.ModelForm):
    class Meta:
        model = RiskEvaluation
        fields = ['factor', 'descripcion', 'imagen']
        widgets = {
            'factor': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
class FiltroRiesgosForm(forms.Form):
    empleado = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(role='empleado'),
        required=False,
        label='Empleado'
    )
    factor = forms.ChoiceField(
        choices=[('', 'Todos')] + RiskEvaluation.FACTORES,
        required=False,
        label='Factor de Riesgo'
    )
    fecha_inicio = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Desde'
    )
    fecha_fin = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Hasta'
    )