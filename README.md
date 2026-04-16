## *📚 Biblioteca Personal API (FastAPI + MySQL)*

## 🚀 Descripción

Biblioteca Personal API es un backend REST desarrollado con FastAPI para la gestión de libros personales.

Permite realizar operaciones CRUD completas conectadas a una base de datos MySQL, con arquitectura profesional basada en capas.

## ⚙️ Tecnologías:
⚡ FastAPI
🐍 Python 3.10+
🗄️ MySQL
🧬 SQLAlchemy
🔄 Alembic
📦 Pydantic
🔐 python-dotenv
🔌 PyMySQL
🌐 CORS Middleware

## 📦 Instalación
1️⃣ Clonar repositorio
```
git clone https://github.com/Valduz-Jose/biblioteca_fastapi.git
cd biblioteca_fastapi
```
2️⃣ Crear entorno virtual

```
python -m venv venv

```
Activar:

```
Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

```
3️⃣ Instalar dependencias

```
pip install -r requirements.txt

```

## ⚙️ Variables de entorno

Crear archivo .env:

```
DB_USER=root
DB_PASSWORD=admin
DB_HOST=localhost
DB_PORT=3306
DB_NAME=biblioteca_db

```
## 🗄️ Base de datos

```
CREATE DATABASE biblioteca_db;

```
## 🚀 Ejecutar proyecto

```
uvicorn main:app --reload --port 8080

```
## 🌐 URLs del sistema

Servicio	URL
* API	http://localhost:8080
* Docs Swagger	http://localhost:8080/docs
* Redoc	http://localhost:8080/redoc
* Endpoint Libros	http://localhost:8080/api/libros

## 📚 Endpoints
* Método	Endpoint	Descripción
* GET	/api/libros	Listar libros
* GET	/api/libros/{id}	Obtener libro
* POST	/api/libros	Crear libro
* PUT	/api/libros/{id}	Actualizar libro
* DELETE	/api/libros/{id}	Eliminar libro

## 📌 Ejemplo JSON

```
{
  "titulo": "Clean Code",
  "autor": "Robert C. Martin",
  "rating": 5
}

```
## 🧠 Arquitectura
```
biblioteca_fastapi/
│
├── api/              # Rutas (controllers)
├── services/         # Lógica de negocio
├── models/           # Modelos ORM
├── schemas.py       # Validaciones Pydantic
├── database.py      # Conexión MySQL
├── main.py          # Entry point
├── alembic/         # Migraciones
├── .env
```
## 🔐 CORS habilitado

✔ React (Vite)
✔ Angular

http://localhost:5173
http://localhost:4200

## 🧪 Ejemplo de uso
Crear libro

```
POST /api/libros
{
  "titulo": "El Principito",
  "autor": "Antoine de Saint-Exupéry",
  "rating": 5
}

```
Respuesta

```
{
  "id": 1,
  "titulo": "El Principito",
  "autor": "Antoine de Saint-Exupéry",
  "rating": 5
}

```
## 📈 Estado del proyecto
* ✅ CRUD completo
* ✅ API REST funcional
* ✅ MySQL integrado
* ✅ Arquitectura profesional
* ✅ Lista para frontend

## 🚀 Próximas mejoras
* 🔐 Autenticación JWT
* 👤 Usuarios y roles
* 🐳 Docker
* ☁️ Deploy en cloud (Render / Railway)
* ⚛️ Frontend en React o Angular

## 👨‍💻 Autor
José Alejandro Valduz Contreras
GitHub: Valduz-Jose

## ⭐ Support
Si este proyecto te ayuda, ¡dale una estrella al repo!

<img width="1835" height="856" alt="Captura de pantalla 2026-04-16 143925" src="https://github.com/user-attachments/assets/78204f95-f8d0-4309-9e5a-44bcb29fe0ef" />
<img width="559" height="830" alt="Captura de pantalla 2026-04-16 143905" src="https://github.com/user-attachments/assets/a16d0632-8c43-4c7a-9029-7a3e78385d6c" />
<img width="418" height="157" alt="Captura de pantalla 2026-04-16 143848" src="https://github.com/user-attachments/assets/f66dd33f-2025-425c-ad30-1d2087a1d45f" />
