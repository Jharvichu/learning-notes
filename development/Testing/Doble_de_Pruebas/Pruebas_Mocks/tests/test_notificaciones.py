from notificaciones import notificar_por_correo, mostrar_configuracion, notificar_por_sms
from unittest.mock import Mock, patch

def test_notificar_por_correo():
    mock_envio = Mock()
    mock_envio.return_value = "Correo simulado enviado"

    notificar_por_correo("Jharvy","jharvy.cadilo.t@uni.pe", mock_envio)
    
    assert mock_envio.called
    assert mock_envio.call_count == 1
    mock_envio.assert_called_with("jharvy.cadilo.t@uni.pe", "Hola Jharvy, Bienvenido a la app.")

@patch("notificaciones.leer_archivo_config")
def test_mostrar_configuracion(mock_leer):
    mock_leer.return_value = "modo=debug\ncolor=azul"

    resultado = mostrar_configuracion()

    assert resultado == "Configuración actual: \nmodo=debug\ncolor=azul"
    mock_leer.assert_called_once()

def test_notificar_por_sms():
    mock_sms = Mock()
    mock_sms.side_effect = [Exception("Error de red"), "SMS enviado"]

    resultado1 = notificar_por_sms("Jharvy","jharvy.cadilo.t@uni.pe", mock_sms)
    resultado2 = notificar_por_sms("Jharvy","jharvy.cadilo.t@uni.pe", mock_sms)

    assert "Error al enviar SMS: Error de red" == resultado1
    assert resultado2 == "SMS enviado"
    assert mock_sms.call_count == 2    

