# Datos de Ejemplo para Pruebas

Este documento contiene datos de ejemplo que puedes usar para probar el sistema después de ejecutar las migraciones.

## Pasos para Cargar Datos de Ejemplo

1. Ejecutar las migraciones:
   ```bash
   python manage.py migrate
   ```

2. Crear un superusuario:
   ```bash
   python manage.py createsuperuser
   ```

3. Acceder al panel de administración en http://127.0.0.1:8000/admin/ y cargar los siguientes datos:

## Marcas

| Nombre | País de Origen | Año de Fundación |
|--------|----------------|------------------|
| Toyota | Japón | 1937 |
| Ford | Estados Unidos | 1903 |
| Volkswagen | Alemania | 1937 |
| Fiat | Italia | 1899 |
| Chevrolet | Estados Unidos | 1911 |

## Modelos

| Marca | Nombre | Año | Combustible | Precio de Lista | Stock |
|-------|--------|-----|-------------|-----------------|-------|
| Toyota | Corolla | 2023 | Nafta | 15000000 | 5 |
| Toyota | Hilux | 2023 | Diesel | 25000000 | 3 |
| Ford | Ranger | 2023 | Diesel | 22000000 | 4 |
| Volkswagen | Amarok | 2023 | Diesel | 28000000 | 2 |
| Fiat | Cronos | 2023 | Nafta | 8000000 | 6 |
| Chevrolet | Onix | 2023 | Nafta | 9000000 | 5 |
| Toyota | Prius | 2023 | Híbrido | 18000000 | 2 |
| Volkswagen | e-Golf | 2023 | Eléctrico | 20000000 | 1 |

## Vendedores

| Nombre | Apellido | Legajo | Fecha de Ingreso |
|--------|----------|--------|------------------|
| Juan | Pérez | V001 | 2020-01-15 |
| María | González | V002 | 2021-03-20 |
| Carlos | Rodríguez | V003 | 2019-06-10 |
| Ana | Martínez | V004 | 2022-02-01 |

## Clientes

| Nombre | Apellido | DNI | Teléfono | Email |
|--------|----------|-----|----------|-------|
| Pedro | López | 12345678 | 11-1234-5678 | pedro.lopez@email.com |
| Laura | Fernández | 23456789 | 11-2345-6789 | laura.fernandez@email.com |
| Roberto | Sánchez | 34567890 | 11-3456-7890 | roberto.sanchez@email.com |
| Sofía | Torres | 45678901 | 11-4567-8901 | sofia.torres@email.com |

## Ventas de Ejemplo

Después de cargar los datos anteriores, puedes crear ventas de ejemplo:

1. Vendedor: Juan Pérez
2. Cliente: Pedro López
3. Modelo: Toyota Corolla 2023
4. Fecha: Fecha actual
5. Precio Final: 14500000
6. Método de Pago: Contado
7. Observaciones: Venta directa, sin financiación

**Nota**: Al registrar esta venta, el stock del Toyota Corolla se reducirá automáticamente de 5 a 4 unidades.

## Verificación

Después de cargar los datos:

1. Verifica que las marcas se muestren correctamente en `/marcas/`
2. Verifica que los modelos se muestren con su stock en `/modelos/`
3. Verifica que puedas crear una venta en `/ventas/nueva/`
4. Verifica que el stock se descuente automáticamente después de crear una venta
5. Verifica que no puedas crear una venta de un modelo sin stock

