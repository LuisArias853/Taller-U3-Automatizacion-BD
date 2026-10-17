import os
from datetime import date

from dotenv import load_dotenv
from faker import Faker
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


def main():
    # 1. Cargar las variables del archivo .env
    load_dotenv()

    host = os.getenv("DB_HOST", "localhost")
    port = int(os.getenv("DB_PORT", "3306"))
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME", "taller_u3")

    if not user or not password:
        raise ValueError(
            "Faltan DB_USER o DB_PASSWORD en el archivo .env"
        )

    # 2. Configurar la conexion con MySQL
    connection_url = URL.create(
        drivername="mysql+pymysql",
        username=user,
        password=password,
        host=host,
        port=port,
        database=database,
        query={"charset": "utf8mb4"},
    )

    engine = create_engine(
        connection_url,
        pool_pre_ping=True,
    )

    # 3. Crear la tabla si no existe
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS personas_LuisMiguel (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        apellido VARCHAR(100) NOT NULL,
        correo VARCHAR(150) NOT NULL,
        telefono VARCHAR(30),
        fecha_nacimiento DATE,
        ciudad VARCHAR(100),
        pais VARCHAR(100),
        profesion VARCHAR(100)
    ) ENGINE=InnoDB
    """

    cantidad_total = 100_000
    tamano_lote = 5_000

    # Faker en español
    fake = Faker("es_CO")

    try:
        with engine.begin() as conn:
            conn.execute(text(create_table_sql))
            print("Tabla personas_LuisMiguel lista.")

            # 4. Generar e insertar 100.000 registros
            for inicio in range(0, cantidad_total, tamano_lote):
                fin = min(inicio + tamano_lote, cantidad_total)

                personas = []

                for _ in range(inicio, fin):
                    personas.append({
                        "nombre": fake.first_name(),
                        "apellido": fake.last_name(),
                        "correo": fake.unique.email(),
                        "telefono": fake.phone_number()[:30],
                        "fecha_nacimiento": fake.date_of_birth(
                            minimum_age=18,
                            maximum_age=80,
                        ),
                        "ciudad": fake.city(),
                        "pais": fake.current_country(),
                        "profesion": fake.job(),
                    })

                conn.execute(
                    text("""
                        INSERT INTO personas_LuisMiguel
                        (nombre, apellido, correo, telefono,
                         fecha_nacimiento, ciudad, pais, profesion)
                        VALUES
                        (:nombre, :apellido, :correo, :telefono,
                         :fecha_nacimiento, :ciudad, :pais, :profesion)
                    """),
                    personas,
                )

                print(f"Insertados {fin:,} de {cantidad_total:,}")

        print("Proceso terminado correctamente.")
        print("Se insertaron 100.000 personas.")

    finally:
        engine.dispose()


if __name__ == "__main__":
    main()