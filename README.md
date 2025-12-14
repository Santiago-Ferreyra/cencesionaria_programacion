# Sistema de Gestión de Concesionaria de Autos

Sistema web desarrollado con Django para gestionar una concesionaria de automóviles. Permite registrar marcas de vehículos, modelos disponibles en stock, vendedores, clientes y las ventas realizadas.

## Características

- **Gestión de Marcas**: Registro de marcas con país de origen y año de fundación
- **Gestión de Modelos**: Control de modelos con información de combustible, precio y stock
- **Gestión de Vendedores**: Registro de vendedores con legajo y fecha de ingreso
- **Gestión de Clientes**: Base de datos de clientes con DNI, teléfono y email
- **Gestión de Ventas**: Registro de ventas con descuento automático de stock
- **Panel de Administración**: Interfaz Django Admin para todas las entidades

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd concesionaria
   ```

2. **Crear un entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual**
   
   En Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   En Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

4. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecutar las migraciones**
   ```bash
   python manage.py migrate
   ```

6. **Crear un superusuario (opcional, para acceder al panel de administración)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Ejecutar el servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

8. **Acceder a la aplicación**
   - Aplicación web: http://127.0.0.1:8000/
   - Panel de administración: http://127.0.0.1:8000/admin/

## Estructura del Proyecto

```
concesionaria/
├── concesionaria_project/    # Configuración del proyecto Django
│   ├── settings.py           # Configuración principal
│   ├── urls.py               # URLs principales
│   └── wsgi.py               # Configuración WSGI
├── ventas/                   # Aplicación principal
│   ├── models.py             # Modelos de datos
│   ├── views.py              # Vistas basadas en clases
│   ├── forms.py              # Formularios
│   ├── admin.py              # Configuración del admin
│   ├── urls.py               # URLs de la aplicación
│   └── templates/            # Templates HTML
│       ├── base.html         # Template base con herencia
│       └── ventas/           # Templates específicos
├── manage.py                 # Script de gestión de Django
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Este archivo
```

## Modelos de Datos

### Marca
- `nombre`: Nombre de la marca (único)
- `pais_origen`: País de origen
- `año_fundacion`: Año de fundación

### Modelo
- `marca`: Relación ForeignKey con Marca
- `nombre`: Nombre del modelo
- `año`: Año del modelo
- `tipo_combustible`: Nafta, Diesel, Eléctrico o Híbrido
- `precio_lista`: Precio de lista
- `cantidad_stock`: Cantidad disponible en stock

### Vendedor
- `nombre`: Nombre del vendedor
- `apellido`: Apellido del vendedor
- `legajo`: Legajo único
- `fecha_ingreso`: Fecha de ingreso a la empresa

### Cliente
- `nombre`: Nombre del cliente
- `apellido`: Apellido del cliente
- `dni`: DNI único
- `telefono`: Teléfono de contacto
- `email`: Email de contacto

### Venta
- `vendedor`: Relación ForeignKey con Vendedor
- `cliente`: Relación ForeignKey con Cliente
- `modelo`: Relación ForeignKey con Modelo
- `fecha_venta`: Fecha de la venta
- `precio_final`: Precio final negociado
- `metodo_pago`: Contado, Financiado o Permuta
- `observaciones`: Observaciones adicionales

**Nota importante**: Al registrar una venta, el sistema automáticamente descuenta una unidad del stock del modelo vendido.

## Funcionalidades Implementadas

- ✅ Vistas basadas en clases (ListView y CreateView) para todas las entidades
- ✅ Templates con herencia usando base.html
- ✅ Formularios con validaciones básicas
- ✅ Panel de administración configurado para todas las entidades
- ✅ Descuento automático de stock al registrar ventas
- ✅ Validación de stock antes de permitir ventas
- ✅ Interfaz responsive con Bootstrap 5

## Uso

1. **Registrar una Marca**: Navegar a "Marcas" → "Nueva Marca"
2. **Registrar un Modelo**: Navegar a "Modelos" → "Nuevo Modelo" (requiere una marca existente)
3. **Registrar un Vendedor**: Navegar a "Vendedores" → "Nuevo Vendedor"
4. **Registrar un Cliente**: Navegar a "Clientes" → "Nuevo Cliente"
5. **Registrar una Venta**: Navegar a "Ventas" → "Nueva Venta" (requiere vendedor, cliente y modelo con stock)

## Notas para el Desarrollo

- El proyecto utiliza SQLite como base de datos por defecto
- Los templates utilizan Bootstrap 5 desde CDN
- El código está diseñado para ser simple y fácil de entender
- Todas las vistas utilizan clases genéricas de Django (ListView, CreateView)

## Autor

Desarrollado para el examen de Programación 3 - Django

