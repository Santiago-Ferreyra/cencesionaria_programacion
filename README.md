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

**Nota importante**: Al registrar una venta, el sistema automáticamente descuenta una unidad del stock del modelo vendido.

## Notas para el Desarrollo

- El proyecto utiliza SQLite como base de datos por defecto
- Los templates utilizan Bootstrap 5 desde CDN
