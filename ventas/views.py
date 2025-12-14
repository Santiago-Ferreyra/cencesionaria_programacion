from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Marca, Modelo, Vendedor, Cliente, Venta
from .forms import MarcaForm, ModeloForm, VendedorForm, ClienteForm, VentaForm


class MarcaListView(ListView):
    """Vista para listar todas las marcas"""
    model = Marca
    template_name = 'ventas/marca_list.html'
    context_object_name = 'marcas'
    paginate_by = 10


class MarcaCreateView(CreateView):
    """Vista para crear una nueva marca"""
    model = Marca
    form_class = MarcaForm
    template_name = 'ventas/marca_form.html'
    success_url = reverse_lazy('marca_list')

    def form_valid(self, form):
        messages.success(self.request, 'Marca creada exitosamente.')
        return super().form_valid(form)


class ModeloListView(ListView):
    """Vista para listar todos los modelos"""
    model = Modelo
    template_name = 'ventas/modelo_list.html'
    context_object_name = 'modelos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('marca')
        return queryset


class ModeloCreateView(CreateView):
    """Vista para crear un nuevo modelo"""
    model = Modelo
    form_class = ModeloForm
    template_name = 'ventas/modelo_form.html'
    success_url = reverse_lazy('modelo_list')

    def form_valid(self, form):
        messages.success(self.request, 'Modelo creado exitosamente.')
        return super().form_valid(form)


class VendedorListView(ListView):
    """Vista para listar todos los vendedores"""
    model = Vendedor
    template_name = 'ventas/vendedor_list.html'
    context_object_name = 'vendedores'
    paginate_by = 10


class VendedorCreateView(CreateView):
    """Vista para crear un nuevo vendedor"""
    model = Vendedor
    form_class = VendedorForm
    template_name = 'ventas/vendedor_form.html'
    success_url = reverse_lazy('vendedor_list')

    def form_valid(self, form):
        messages.success(self.request, 'Vendedor creado exitosamente.')
        return super().form_valid(form)


class ClienteListView(ListView):
    """Vista para listar todos los clientes"""
    model = Cliente
    template_name = 'ventas/cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 10


class ClienteCreateView(CreateView):
    """Vista para crear un nuevo cliente"""
    model = Cliente
    form_class = ClienteForm
    template_name = 'ventas/cliente_form.html'
    success_url = reverse_lazy('cliente_list')

    def form_valid(self, form):
        messages.success(self.request, 'Cliente creado exitosamente.')
        return super().form_valid(form)


class VentaListView(ListView):
    """Vista para listar todas las ventas"""
    model = Venta
    template_name = 'ventas/venta_list.html'
    context_object_name = 'ventas'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('vendedor', 'cliente', 'modelo__marca')
        return queryset


class VentaCreateView(CreateView):
    """Vista para crear una nueva venta"""
    model = Venta
    form_class = VentaForm
    template_name = 'ventas/venta_form.html'
    success_url = reverse_lazy('venta_list')

    def form_valid(self, form):
        messages.success(self.request, 'Venta registrada exitosamente. El stock ha sido actualizado.')
        return super().form_valid(form)


class HomeView(TemplateView):
    """Vista para la página de inicio con dashboard"""
    template_name = 'ventas/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_marcas'] = Marca.objects.count()
        context['total_modelos'] = Modelo.objects.count()
        context['total_vendedores'] = Vendedor.objects.count()
        context['total_clientes'] = Cliente.objects.count()
        context['total_ventas'] = Venta.objects.count()
        context['modelos_stock'] = Modelo.objects.filter(cantidad_stock__gt=0).count()
        context['ultimas_ventas'] = Venta.objects.select_related('vendedor', 'cliente', 'modelo__marca')[:5]
        return context

