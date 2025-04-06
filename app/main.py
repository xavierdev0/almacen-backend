from fastapi import FastAPI
from app.core.database import create_db_and_tables
from app.models.usuario_model import Usuario

app = FastAPI(title="Almacen API")

@app.on_event("startup")
def on_startup():
    # Importa todos los modelos antes de crear las tablas
    # La importación de Usuario ya está hecha arriba
    create_db_and_tables()


@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API del almacén"}


# Para ejecutar manualmente la creación de tablas, puedes usar este código:
if __name__ == "__main__":
    # Asegúrate de que todos los modelos están importados
    print("Creando tablas en la base de datos...")
    create_db_and_tables()
    print("¡Tablas creadas exitosamente!")
