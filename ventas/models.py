from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class Marca(models.Model):
    """Representa una marca de vehículos"""
    nombre = models.CharField(max_length=100, unique=True)
    pais_origen = models.CharField(max_length=100)
    año_fundacion = models.IntegerField(
        validators=[MinValueValidator(1800), MaxValueValidator(2100)]
    )

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.pais_origen})"


class Modelo(models.Model):
    """Representa un modelo de vehículo"""
    TIPO_COMBUSTIBLE_CHOICES = [
        ('nafta', 'Nafta'),
        ('diesel', 'Diesel'),
        ('electrico', 'Eléctrico'),
        ('hibrido', 'Híbrido'),
    ]

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='modelos')
    nombre = models.CharField(max_length=100)
    año = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2100)]
    )
    tipo_combustible = models.CharField(max_length=20, choices=TIPO_COMBUSTIBLE_CHOICES)
    precio_lista = models.DecimalField(
        max_digits=12, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    cantidad_stock = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"
        ordering = ['marca', 'nombre']
        unique_together = [['marca', 'nombre', 'año']]

    def __str__(self):
        return f"{self.marca.nombre} {self.nombre} ({self.año})"


class Vendedor(models.Model):
    """Representa un vendedor de la concesionaria"""
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    legajo = models.CharField(max_length=20, unique=True)
    fecha_ingreso = models.DateField()

    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f"{self.apellido}, {self.nombre} (Legajo: {self.legajo})"


class Cliente(models.Model):
    """Representa un cliente de la concesionaria"""
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f"{self.apellido}, {self.nombre} (DNI: {self.dni})"


class Venta(models.Model):
    """Representa una venta de un vehículo"""
    METODO_PAGO_CHOICES = [
        ('contado', 'Contado'),
        ('financiado', 'Financiado'),
        ('permuta', 'Permuta'),
    ]

    vendedor = models.ForeignKey(Vendedor, on_delete=models.PROTECT, related_name='ventas')
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='compras')
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name='ventas')
    fecha_venta = models.DateField()
    precio_final = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO_CHOICES)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ['-fecha_venta', '-id']

    def __str__(self):
        return f"Venta #{self.id} - {self.modelo} a {self.cliente}"

    def clean(self):
        """Valida que haya stock disponible antes de permitir la venta"""
        if self.modelo and self.modelo.cantidad_stock < 1:
            raise ValidationError({
                'modelo': 'No hay stock disponible para este modelo.'
            })

    def save(self, *args, **kwargs):
        """Sobrescribe save para descontar stock al crear una venta"""
        # Si es una nueva venta (no tiene pk), descontar stock
        if not self.pk:
            # Validar que haya stock disponible
            if self.modelo.cantidad_stock < 1:
                raise ValidationError('No hay stock disponible para este modelo.')
            # Descontar una unidad del stock
            self.modelo.cantidad_stock -= 1
            self.modelo.save(update_fields=['cantidad_stock'])
        super().save(*args, **kwargs)

