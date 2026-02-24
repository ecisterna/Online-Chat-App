# Guía de Despliegue en Render

## 📦 Archivos de Configuración

- ✅ `Procfile` - Comando para iniciar la aplicación
- ✅ `runtime.txt` - Versión de Python
- ✅ `requirements.txt` - Dependencias con gunicorn y eventlet
- ✅ `.env.example` - Ejemplo de variables de entorno
- ✅ `main.py` - Configurado para usar variables de entorno

## 🚀 Pasos para Desplegar

### 1. Crear cuenta en Render
1. Ve a [render.com](https://render.com)
2. Inicia sesión con GitHub

### 2. Crear un nuevo Web Service
1. Haz clic en **"New +"** → **"Web Service"**
2. Conecta tu repositorio `Online-Chat-App`
3. Configura los campos:
   - **Name**: `online-chat-app` (o el nombre que quieras)
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --worker-class eventlet -w 1 --bind 0.0.0.0:$PORT main:app`

### 3. Configurar Variables de Entorno
En la sección **"Environment Variables"**, añade:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | tu clave secreta (ver abajo) |
| `PYTHON_VERSION` | `3.11.0` |

Para generar una `SECRET_KEY` segura, ejecuta en tu terminal:
```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

### 4. Seleccionar Plan
- Selecciona el plan **Free** para empezar
- Haz clic en **"Create Web Service"**

### 5. Esperar el Despliegue
Render instalará dependencias y desplegará tu app en ~3-5 minutos.
En los logs deberías ver: `Database tables created successfully!` ✅

## 🗄️ Agregar Base de Datos PostgreSQL (Recomendado)

Con SQLite los datos se pierden en cada redespliegue. Para persistencia usa PostgreSQL:

1. En tu dashboard de Render, haz clic en **"New +"** → **"PostgreSQL"**
2. Configura:
   - **Name**: `online-chat-db`
   - **Plan**: Free
3. Haz clic en **"Create Database"**
4. Una vez creada, copia la **"Internal Database URL"**
5. Ve a tu Web Service → **"Environment"** → añade:
   - `DATABASE_URL` = (pega la URL copiada)
6. Render redesplegará automáticamente

## 🔄 Actualizar la Aplicación

Cualquier push a `main` redesplegará automáticamente:

```bash
git add .
git commit -m "descripción de los cambios"
git push origin main
```

## ⚠️ Notas Importantes

- El plan **Free** de Render hace que la app se **duerma** tras 15 minutos de inactividad
- Al recibir una petición después de estar dormida, tarda ~30 segundos en reactivarse
- Los datos en **SQLite se pierden** en cada redespliegue → usa PostgreSQL para producción
- El plan Free incluye **750 horas/mes** de uso gratuito

## 🔍 Solución de Problemas

### La app tarda en responder
- Normal en el plan Free: la app se "duerme" por inactividad
- Espera ~30 segundos la primera vez

### Internal Server Error
- Revisa los logs en Render → tu servicio → **"Logs"**
- Verifica que `DATABASE_URL` esté configurada correctamente

### WebSockets no funcionan
- Render soporta WebSockets de forma nativa ✅
- Asegúrate de usar el comando de inicio con `eventlet`

### "No module named X"
- Verifica que el paquete esté en `requirements.txt`
- Fuerza un nuevo despliegue desde el dashboard

## 📞 Recursos

- [Documentación de Render](https://render.com/docs)
- [Render + Flask](https://render.com/docs/deploy-flask)
- [Documentación de Flask-SocketIO](https://flask-socketio.readthedocs.io)

---

¡Buena suerte con tu despliegue! 🎉
