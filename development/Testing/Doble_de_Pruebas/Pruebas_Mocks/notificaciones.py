from lector import leer_archivo_config

def enviar_correo(destinatario, mensaje):
     print(f"Enviando correo a {destinatario}: {mensaje}")

def enviar_sms(destinatario, mensaje):
     print(f"Enviando SMS a {destinatario}: {mensaje}")

def notificar_por_correo(nombre, correo, enviar_correo):
     mensaje = f"Hola {nombre}, Bienvenido a la app."
     enviar_correo(correo, mensaje)

def notificar_por_sms(nombre, correo, enviar_sms):
     try:
          resultado = enviar_sms(correo, f"Hola {nombre}, tu codigo es 1234.")
          return resultado
     except Exception as e:
          return f"Error al enviar SMS: {e}"          


def mostrar_configuracion():
    contenido = leer_archivo_config()
    return f"Configuración actual: \n{contenido}"
