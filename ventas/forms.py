from django import forms
from .models import Marca, Modelo, Vendedor, Cliente, Venta


class MarcaForm(forms.ModelForm):
    """Formulario para crear y editar marcas"""
    class Meta:
        model = Marca
        fields = ['nombre', 'pais_origen', 'año_fundacion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'pais_origen': forms.TextInput(attrs={'class': 'form-control'}),
            'año_fundacion': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre:
            nombre = nombre.strip().title()
        return nombre


class ModeloForm(forms.ModelForm):
    """Formulario para crear y editar modelos"""
    class Meta:
        model = Modelo
        fields = ['marca', 'nombre', 'año', 'tipo_combustible', 'precio_lista', 'cantidad_stock']
        widgets = {
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_combustible': forms.Select(attrs={'class': 'form-control'}),
            'precio_lista': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'cantidad_stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre:
            nombre = nombre.strip()
        return nombre


class VendedorForm(forms.ModelForm):
    """Formulario para crear y editar vendedores"""
    class Meta:
        model = Vendedor
        fields = ['nombre', 'apellido', 'legajo', 'fecha_ingreso']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'legajo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre:
            nombre = nombre.strip().title()
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if apellido:
            apellido = apellido.strip().title()
        return apellido


class ClienteForm(forms.ModelForm):
    """Formulario para crear y editar clientes"""
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'dni', 'telefono', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre:
            nombre = nombre.strip().title()
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if apellido:
            apellido = apellido.strip().title()
        return apellido


class VentaForm(forms.ModelForm):
    """Formulario para crear y editar ventas"""
    class Meta:
        model = Venta
        fields = ['vendedor', 'cliente', 'modelo', 'fecha_venta', 'precio_final', 'metodo_pago', 'observaciones']
        widgets = {
            'vendedor': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'modelo': forms.Select(attrs={'class': 'form-control'}),
            'fecha_venta': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'precio_final': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'metodo_pago': forms.Select(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo modelos con stock disponible
        self.fields['modelo'].queryset = Modelo.objects.filter(cantidad_stock__gt=0)

    def clean(self):
        cleaned_data = super().clean()
        modelo = cleaned_data.get('modelo')
        
        if modelo and modelo.cantidad_stock < 1:
            raise forms.ValidationError({
                'modelo': 'No hay stock disponible para este modelo.'
            })
        
        return cleaned_data

