# futbol-api

## Instalación

Para empezar, sigue los siguientes pasos:

1. Clonar el repositorio:

    ```bash
   https://github.com/cgabriel124/futbol_api.git
   ```

2. Abrir el directorio del proyecto:

   ```bash
   cd futbol_api
   ```

3. Instalar las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

Esto instalara todos los paquetes necesarios que permitiran correr el proyecto.

## Información sobre la base de datos

La api trabaja sobre una base de datos local PostgreSQL v16.0, por lo que es necesario tener una ya creada en el
ordenador. Por defecto la base de datos tiene el nombre "db_futbol".

## Configuración del archivo .env y Ejecución del proyecto

El proyecto utiliza un archivo .env para almacenar claves secretas y configuraciones sensibles. Sigue estos pasos para
configurarlo correctamente:

1. Renombra el archivo `.env.example` a `.env`.
2. Abre el archivo `.env` y completa los valores de las variables con la información correcta(sin comillas).
3. Guarda el archivo.
4. Ejecuta el comando `python manage.py migrate` para crear las tablas en la base de datos.
5. Ejecuta el comando `python manage.py runserver` para iniciar el servidor.
