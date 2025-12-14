# Instrucciones para Configurar Git

Este documento explica cómo inicializar el repositorio Git y realizar commits descriptivos.

## Inicializar el Repositorio

1. **Inicializar Git en el proyecto**
   ```bash
   cd concesionaria
   git init
   ```

2. **Configurar tu usuario de Git (si no lo has hecho antes)**
   ```bash
   git config user.name "Tu Nombre"
   git config user.email "tu.email@ejemplo.com"
   ```

3. **Agregar todos los archivos al staging**
   ```bash
   git add .
   ```

4. **Realizar el primer commit**
   ```bash
   git commit -m "Inicializar proyecto Django - Sistema de Gestión de Concesionaria"
   ```

## Ejemplo de Commits Descriptivos

A continuación se muestran ejemplos de commits que reflejan el proceso de desarrollo:

```bash
# Commit inicial
git commit -m "Inicializar proyecto Django - Sistema de Gestión de Concesionaria"

# Crear modelos
git add ventas/models.py
git commit -m "Crear modelos: Marca, Modelo, Vendedor, Cliente y Venta con relaciones"

# Configurar admin
git add ventas/admin.py
git commit -m "Configurar panel de administración para todas las entidades"

# Crear vistas
git add ventas/views.py ventas/urls.py
git commit -m "Implementar vistas basadas en clases (ListView y CreateView) para todas las entidades"

# Crear formularios
git add ventas/forms.py
git commit -m "Crear formularios con validaciones para todas las entidades"

# Crear templates
git add ventas/templates/
git commit -m "Crear templates con herencia usando base.html y Bootstrap 5"

# Implementar lógica de stock
git add ventas/models.py
git commit -m "Implementar descuento automático de stock al registrar venta"

# Documentación
git add README.md requirements.txt .gitignore
git commit -m "Agregar documentación, requirements.txt y .gitignore"
```

## Subir a GitHub/GitLab

1. **Crear un repositorio en GitHub o GitLab** (no inicializar con README)

2. **Agregar el remote**
   ```bash
   git remote add origin <URL_DEL_REPOSITORIO>
   ```

3. **Subir los commits**
   ```bash
   git branch -M main
   git push -u origin main
   ```

## Importante

- **Todos los commits deben ser realizados con tu usuario de Git**
- **Los mensajes de commit deben ser descriptivos** y explicar qué se hizo
- **No subas archivos sensibles** (db.sqlite3, archivos de entorno virtual, etc.)
- El archivo `.gitignore` ya está configurado para excluir estos archivos

