# Taller U3 — Automatización de BD con Python, Faker y Git

## Descripción

Este proyecto automatiza la creación y el poblado de una tabla
MySQL mediante Python, SQLAlchemy y Faker.

La tabla `personas_LuisMiguel` contiene 100.000 registros ficticios
con información como nombre, apellido, correo, teléfono,
fecha de nacimiento, ciudad, país y profesión.

## Tecnologías utilizadas

- Python 3.10 o superior
- MySQL
- SQLAlchemy
- Faker
- PyMySQL
- python-dotenv
- Git y GitHub

## Requisitos previos

- Tener Python y MySQL instalados.
- Tener creada la base de datos `taller_u3`.
- Tener Git instalado.

## Instalación

1. Clonar el repositorio:

   git clone https://github.com/LuisArias853/Taller-U3-Automatizacion-BD

2. Entrar en la carpeta del proyecto:

   cd Taller_U3

3. Crear el entorno virtual:

   python -m venv .venv

4. Activar el entorno virtual en Windows:

   .venv\Scripts\activate

5. Instalar las dependencias:

   python -m pip install -r requirements.txt

6. Crear un archivo `.env` a partir de `.env.example`.
   Configurar las credenciales de MySQL en el archivo `.env`.

## Configuración de la base de datos

Crear la base de datos ejecutando en MySQL:

    CREATE DATABASE taller_u3;

Verificar que las variables de conexión en `.env` coincidan
con la configuración local de MySQL.

## Ejecución

Ejecutar el programa desde la carpeta del proyecto:

    python main.py

El programa crea la tabla si no existe y genera e inserta
100.000 registros ficticios en lotes de 5.000.

## Verificación

Ejecutar en DBeaver:

    SELECT COUNT(*) FROM personas_ariadne;

El resultado esperado es 100.000 registros.

## Seguridad

El archivo `.env` contiene credenciales privadas y está
excluido del repositorio mediante `.gitignore`.

El archivo `.env.example` proporciona una plantilla
sin credenciales reales.