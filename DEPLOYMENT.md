# Guía de Despliegue en Railway

## 📦 Preparación Completada

Tu aplicación ya está lista para desplegarse en Railway. Los siguientes archivos han sido creados/actualizados:

- ✅ `Procfile` - Comando para iniciar la aplicación
- ✅ `railway.json` - Configuración específica de Railway
- ✅ `runtime.txt` - Versión de Python
- ✅ `requirements.txt` - Actualizado con gunicorn y eventlet
- ✅ `.gitignore` - Archivos a ignorar en git
- ✅ `.env.example` - Ejemplo de variables de entorno
- ✅ `main.py` - Actualizado para usar variables de entorno

## 🚀 Pasos para Desplegar

### 1. Crear cuenta en Railway
1. Ve a [railway.app](https://railway.app)
2. Haz clic en "Start a New Project"
3. Inicia sesión con GitHub

### 2. Conectar tu repositorio
1. Asegúrate de que tu código esté en GitHub:
   ```bash
   git add .
   git commit -m "Preparar para despliegue en Railway"
   git push origin main
   ```

2. En Railway, selecciona "Deploy from GitHub repo"
3. Selecciona el repositorio `Online-Chat-App`

### 3. Configurar Variables de Entorno
En el dashboard de Railway, ve a la pestaña "Variables" y añade:

```
SECRET_KEY=genera_una_clave_secreta_aleatoria_aqui
```

Para generar una clave secreta segura, ejecuta en tu terminal:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 4. Desplegar
Railway desplegará automáticamente tu aplicación. Espera unos minutos.

### 5. Obtener la URL
Una vez desplegado, Railway te dará una URL como: `https://tu-app.up.railway.app`

## 🔧 Características Configuradas

- **Gunicorn con Eventlet**: Servidor de producción optimizado para WebSockets
- **CORS habilitado**: Permite conexiones desde cualquier origen
- **Variables de entorno**: Configuración segura y flexible
- **SQLite**: Base de datos por defecto (puedes migrar a PostgreSQL después)

## 📝 Comandos Útiles

### Probar localmente antes de desplegar:
```bash
# Instalar las nuevas dependencias
pip install -r requirements.txt

# Ejecutar con gunicorn localmente
gunicorn --worker-class eventlet -w 1 --bind 0.0.0.0:5000 main:app
```

### Ver logs en Railway:
Los logs están disponibles en el dashboard de Railway en tiempo real.

## 🔄 Actualizar la Aplicación

Después del primer despliegue, cualquier push a la rama `main` desplegará automáticamente:

```bash
git add .
git commit -m "Descripción de los cambios"
git push origin main
```

## 💡 Próximos Pasos (Opcional)

### Migrar a PostgreSQL
Railway ofrece PostgreSQL gratis:
1. En tu proyecto, haz clic en "+ New"
2. Selecciona "Database" → "Add PostgreSQL"
3. Railway automáticamente creará la variable `DATABASE_URL`
4. Redeploy tu aplicación

### Configurar dominio personalizado
1. Ve a Settings → Domains en Railway
2. Añade tu dominio personalizado

## ⚠️ Notas Importantes

- Railway ofrece **$5 de crédito gratis al mes**
- Después del crédito gratis, necesitarás añadir un método de pago
- La app se suspenderá si no se usa (se reactiva automáticamente)
- Los datos en SQLite se pueden perder en redespliegues (usa PostgreSQL en producción)

## 🆘 Solución de Problemas

### Error: "Application failed to respond"
- Verifica que la variable `PORT` se esté usando correctamente
- Revisa los logs en Railway

### WebSockets no funcionan
- Asegúrate de que `cors_allowed_origins="*"` esté en `SocketIO`
- Verifica que eventlet esté instalado

### La base de datos se resetea
- Cambia a PostgreSQL en lugar de SQLite para persistencia

## 📞 Soporte

Si tienes problemas, revisa:
- [Documentación de Railway](https://docs.railway.app)
- [Documentación de Flask-SocketIO](https://flask-socketio.readthedocs.io)

---

¡Buena suerte con tu despliegue! 🎉
