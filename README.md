# Galería Múltimedia Web

Aplicación Django

# Despliegue Heroku

- Procfile
- requirements.txt
- runtime.txt
- Instalación Gunicorn
- Git-> git push heroku master (Heroku Cli)

- heroku ps:scale web=1 (Heroku Cli)

# Despliegue Base de datos

- Eliminar carpeta Migrations
- Eliminar Base de datos
- Correr sentencia python manage.py makemigrations galleryweb
- Correr sentencia python manage.py migrate galleryweb 0001
- Correr sentencia python manage.py migrate
- Crear superuser (python manage.py createsuperuser)


