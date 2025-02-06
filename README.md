# fastapi
API's on Python with Fastapi

## Instalación
Sigue estos pasos para configurar el entorno de desarrollo:

### Crear un entorno virtual

1. Abre una terminal o línea de comandos.
2. Navega hasta el directorio de tu proyecto.
3. Ejecuta el siguiente comando para crear un entorno virtual llamado `.venv`:

```bash
python3 -m venv .venv
```

### Activar el entorno virtual

En Windows:
```bash
.venv\Scripts\activate
```
En macOS y Linux:
```bash
source .venv/bin/activate
```
### Instalar las dependencias

```bash
pip install -r requirements.txt
```

### Inicia el servidor local

```bash
fastapi dev main.py
```