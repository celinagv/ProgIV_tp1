# TP1 - ABM de Usuarios y Productos con FastAPI

API REST hecha con FastAPI. Almacena los datos en memoria
(se reinician al apagar el servidor).

## Requisitos
- Python 3.12 o superior

## Instalación
```bash
python -m venv .venv
```
Activar el entorno:
- Windows (PowerShell): `.venv\Scripts\Activate.ps1`
- Windows (CMD): `.venv\Scripts\activate.bat`
- Linux/Mac: `source .venv/bin/activate`

```bash
pip install -r requirements.txt
```

## Cómo levantar la aplicación
```bash
fastapi dev main.py
```
La API queda en http://127.0.0.1:8000

## Documentación interactiva (Swagger)
Abrir http://127.0.0.1:8000/docs para probar todos los endpoints.

## Endpoints

### Usuarios
| Verbo | Ruta | Descripción |
|---|---|---|
| GET | /user | Lista usuarios. Filtro opcional `?is_active=true/false` |
| GET | /user/{id} | Obtiene un usuario |
| POST | /user | Crea un usuario (409 si el id existe) |
| PUT | /user/{id} | Modifica un usuario |
| DELETE | /user/{id} | Elimina un usuario |

### Productos
| Verbo | Ruta | Descripción |
|---|---|---|
| GET | /product | Lista productos. Filtro opcional `?categoria=` |
| GET | /product/{id} | Obtiene un producto |
| POST | /product | Crea un producto (409 si el id existe) |
| PUT | /product/{id} | Modifica un producto |
| DELETE | /product/{id} | Elimina un producto |
| PATCH | /product/{id} | Modifica parcialmente un producto |