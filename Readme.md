# Proyecto Maquina Expendedora (Flask + Vue)

# Estructura de carpetas:
```
Sintesis_Proyecto-MaquinaExpendedora/
├── flask-api/          (backend)
│   ├── app.py
│   └── api/
│       └── rutas.py
├── tw-ts-vue/          (frontend)
│   ├── public/
│   ├── src/
│   │   ├── App.vue
│   │   ├── main.js
│   │   └── components/
│   └── package.json
├── README.md
```

# Instalacion:
## Instalacion de Python
https://www.python.org/downloads/

Marcar la opcion de "**Añadir python a las variables de entorno**".

### Instalar VENV
```bash
python.exe -m venv .venv
```

### Instalar Requeriments.txt
```bash
pip install -r .\requirements.txt
```

## Instalacion de NodeJS
https://nodejs.org/en/download

# Iniciar Proyecto
## Flask
```bash
cd flask-api
flask run
```
## Vue
*En otra terminal.*
```bash
cd tw-ts-vue
npm run serve
```

# Deployment
```bash

```