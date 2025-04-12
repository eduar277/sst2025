# Sistema de Gestión de Riesgos SST - Teletrabajo

Este proyecto es una aplicación web para la gestión de evaluaciones de riesgos laborales en empresas que implementan modalidad de teletrabajo.

## 🚀 Requisitos Previos

- Python 3.10+
- pip
- Git
- PostgreSQL o SQLite
- Entorno virtual recomendado (venv)

## ⚙️ Instalación y Despliegue Local

### 1. Clonar el repositorio

```bash
git clone https://github.com/eduar277/sst2025.git
cd sst2025
```

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

> Si no tienes `requirements.txt`, ejecuta `pip freeze > requirements.txt` luego de instalar Django y librerías necesarias.

### 4. Configurar base de datos

Por defecto usa SQLite. Si usas PostgreSQL:

- Configura las variables en `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_db',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear superusuario

```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

Abre en el navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Estructura del Proyecto

- `users/`: autenticación, roles, dashboards
- `risks/`: evaluaciones de riesgos
- `media/`: imágenes cargadas por los usuarios
- `templates/`: archivos HTML del sistema

---

## 🖼️ Funcionalidades Clave

- Registro e inicio de sesión por roles (`empleado`, `empleador`, `admin`)
- Evaluación de riesgos con imágenes adjuntas
- Seguimiento del estado (`pendiente`, `en revisión`, `mitigado`)
- Dashboard por rol con estadísticas (Chart.js)
- Exportación de reportes a PDF
- Sistema de filtros, alertas, y control de acceso

---

## 📦 Despliegue (Opcional)

Puedes usar servicios como:

- [Render](https://render.com/)
- [Railway](https://railway.app/)
- [Heroku](https://www.heroku.com/)
- Servidor propio con Nginx + Gunicorn

---

## 🧑 Autor

Desarrollado por [@eduar277](https://github.com/eduar277)


