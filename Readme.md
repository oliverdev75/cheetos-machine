# Proyecto Maquina Expendedora (Flask + Vue)

# Miro (Organizacion dle proyecto)
https://miro.com/welcome/dlBnaGlPdWdTdnZTNDNiMTZQV0VvZ0dvVjUzU0JzMERmTG5TZkNTTVVkWXJ2NzZHR252ZGgvb2JEUUtpWGhRUG5adURaTU94NmwyM1owdGRoWm1kRU5tc3dDcy8ydCsrRTZVdmJaK3EzV3l2LzJzV1VuZnJyeWkyTVNGYmNZMlJBS2NFMDFkcUNFSnM0d3FEN050ekl3PT0hdjE=?share_link_id=795515166597

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

# Estructura BBDD
## Tablas:
 - Usuarios
 - Productos
 - Pedidos
 - Pedido_Producto

## Relaciones:
 - Usuarios pueden realizar - 0,N -> Pedidos
 - Productos pertenece a - 0,1 -> Usuarios
 - Pedido puede contener - 0,1 -> Productos
 - Producto puede estar en - 0,N -> Pedidos


# Instalacion:
## Instalacion de Python
https://www.python.org/downloads/

Marcar la opcion de "**Añadir python a las variables de entorno**".

### Instalar VENV
```bash
cd flask-api
python.exe -m venv .venv
```

### Instalar Requeriments.txt
```bash
pip install -r .\requirements.txt
```

## Instalacion de NodeJS
https://nodejs.org/en/download

# Iniciar Proyecto
```bash
.\flask-api\.venv\Scripts\activate
cd flask-api
flask run
```
## Iniciar Venv
```bash
.\.venv\Scripts\activate
```

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