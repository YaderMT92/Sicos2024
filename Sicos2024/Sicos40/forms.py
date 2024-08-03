from django import forms
from Sicos40.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['IdCliente','Nombres', 'cedula','LugarTrabajo','Direccion','TipoId','SujetoObligado','Apellidos', 'Categoria']

    # Agregamos un campo para las opciones de categoría
    CATEGORIA_CHOICES = [
        ('cliente', 'CLIENTE'),
        ('pasivo', 'PASIVO'),
    ]
    Categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES)


class BusquedaForm(forms.Form):
    TIPO_BUSQUEDA = (
        ('cliente', 'Cliente'),
        ('poliza', 'Póliza'),
    )
    tipo_busqueda = forms.ChoiceField(choices=TIPO_BUSQUEDA, widget=forms.RadioSelect)
    criterio_busqueda = forms.CharField(max_length=100)
