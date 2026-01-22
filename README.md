# TodoApp - FastAPI Todo Application

Una aplicación de gestión de tareas construida con FastAPI, SQLAlchemy y PostgreSQL.

## Requisitos Previos

- Python 3.8 o superior
- Docker y Docker Compose (para la base de datos)
- pip (gestor de paquetes de Python)

## Configuración del Proyecto

### 1. Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd TodoApp
```

### 2. Crear el Entorno Virtual

En Python, el entorno virtual es equivalente a `node_modules` en Node.js. Mantiene las dependencias aisladas por proyecto.

**En Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

Verás `(venv)` en tu terminal cuando el entorno virtual esté activo.

### 3. Instalar Dependencias

Similar a `npm install` en Node.js:

```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno

Copia el archivo de ejemplo y ajusta las variables según tu configuración:

```bash
cp .env.example .env
```

Edita el archivo `.env` si necesitas cambiar la configuración de la base de datos. Por defecto usa:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/TodoApplicationDatabase
```

### 5. Iniciar la Base de Datos con Docker

El proyecto incluye un archivo `docker-compose.yml` que levanta una base de datos PostgreSQL:

```bash
docker-compose up -d
```

Esto iniciará PostgreSQL en el puerto 5432.

### 6. Ejecutar Migraciones de Base de Datos

Alembic es el equivalente a herramientas como Sequelize o TypeORM en Node.js:

```bash
alembic upgrade head
```

### 7. Iniciar la Aplicación

Similar a `npm start` o `npm run dev`:

```bash
uvicorn main:app --reload
```

La aplicación estará disponible en `http://localhost:8000`

## Documentación de la API

FastAPI genera documentación automática:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Estructura del Proyecto

```
TodoApp/
├── alembic/              # Migraciones de base de datos (como migrations/ en Node.js)
├── routers/              # Rutas de la API (como routes/ en Express)
│   ├── auth.py          # Autenticación
│   ├── todos.py         # Operaciones CRUD de tareas
│   ├── admin.py         # Rutas de administrador
│   └── users.py         # Gestión de usuarios
├── test/                 # Tests (como __tests__/ en Node.js)
├── database.py           # Configuración de la base de datos
├── models.py             # Modelos de SQLAlchemy (como models/ en Sequelize)
├── main.py               # Punto de entrada de la aplicación
├── requirements.txt      # Dependencias (como package.json)
├── .env                  # Variables de entorno (no se commitea)
├── .env.example          # Plantilla de variables de entorno
└── docker-compose.yml    # Configuración de Docker

```

## Comandos Útiles

### Gestión del Entorno Virtual

```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Desactivar entorno virtual
deactivate

# Instalar nueva dependencia y actualizar requirements.txt
pip install <paquete>
pip freeze > requirements.txt
```

### Base de Datos

```bash
# Iniciar PostgreSQL
docker-compose up -d

# Detener PostgreSQL
docker-compose down

# Ver logs de PostgreSQL
docker-compose logs -f postgres

# Crear nueva migración
alembic revision -m "descripción del cambio"

# Aplicar migraciones
alembic upgrade head

# Revertir última migración
alembic downgrade -1
```

### Desarrollo

```bash
# Iniciar servidor de desarrollo con hot-reload
uvicorn main:app --reload

# Iniciar en puerto específico
uvicorn main:app --reload --port 3000

# Ejecutar tests
pytest

# Ejecutar tests con cobertura
pytest --cov
```

## Diferencias Clave con Node.js

| Concepto | Node.js | Python/FastAPI |
|----------|---------|----------------|
| Gestor de paquetes | npm/yarn | pip |
| Archivo de dependencias | package.json | requirements.txt |
| Entorno virtual | node_modules/ | venv/ |
| Variables de entorno | process.env | os.getenv() |
| Librería para .env | dotenv | python-dotenv |
| ORM popular | Sequelize/Prisma | SQLAlchemy |
| Migraciones | Sequelize CLI/Prisma | Alembic |
| Servidor de desarrollo | nodemon | uvicorn --reload |

## Solución de Problemas

### Error: "No module named 'dotenv'"

Asegúrate de que el entorno virtual esté activado e instala las dependencias:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Error de conexión a PostgreSQL

Verifica que Docker esté ejecutándose:

```bash
docker-compose ps
```

Si no está activo, inícialo:

```bash
docker-compose up -d
```

### Puerto 5432 ya en uso

Si ya tienes PostgreSQL instalado localmente, cambia el puerto en `docker-compose.yml` o detén la instancia local.
