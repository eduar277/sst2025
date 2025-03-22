Proyecto SST 2025 - Seguridad y Salud en el Teletrabajo

Este es un sistema de gestión de Seguridad y Salud en el Trabajo (SST) diseñado para pequeñas empresas que implementan el teletrabajo.

Tecnologías Utilizadas

Django (Backend y API REST)

PostgreSQL (Base de datos)

Django REST Framework (Creación de API)

PyCharm (IDE de desarrollo)

GitHub (Control de versiones)

Instalación y Configuración

1. Clonar el repositorio

git clone https://github.com/eduar277/sst2025.git
cd sst2025

2. Crear entorno virtual e instalar dependencias

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Configurar la base de datos PostgreSQL

Edita el archivo settings.py y ajusta la configuración de la base de datos:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sst_db',
        'USER': 'postgres',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

4. Aplicar migraciones y crear un superusuario

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

5. Ejecutar el servidor

python manage.py runserver

Accede a http://127.0.0.1:8000/ para ver la aplicación en acción.

Estructura del Proyecto

sst2025/
│── users/ (Manejo de autenticación y permisos)
│── risks/ (Gestín de riesgos laborales)
│── notifications/ (Alertas y seguimientos)
│── djangoProject/ (Configuraciones principales)
│── manage.py (Comandos de administración de Django)
│── requirements.txt (Dependencias del proyecto)
│── README.md (Este archivo)


Contribuciones

Haz un fork del repositorio.

Crea una rama nueva (git checkout -b nueva-funcionalidad).

Realiza tus cambios y haz commit (git commit -m "Descripción del cambio").

Sube la rama (git push origin nueva-funcionalidad).

Crea un Pull Request.
