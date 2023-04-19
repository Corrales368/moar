from sib_api_v3_sdk import Email, SendSmtpEmail, ApiClient, Configuration
from sib_api_v3_sdk.rest import ApiException

def enviar_correo(destinatario, asunto, cuerpo):
    configuration = Configuration()
    configuration.api_key['api-key'] = 'TU_API_KEY'

    # Crear un objeto ApiClient con la configuración
    api_client = ApiClient(configuration)

    # Crear un objeto SendSmtpEmail con los datos del correo
    send_smtp_email = SendSmtpEmail(
        to=[{'email': destinatario}],
        subject=asunto,
        html_content=cuerpo,
        sender={'email': 'tu_email'}
    )

    # Enviar el correo a través de la API de Sendinblue
    api_instance = Email(api_client)
    try:
        # Llamar al método send_transac_email para enviar el correo
        response = api_instance.send_transac_email(send_smtp_email)
        print(response)
    except ApiException as e:
        print("Error al enviar el correo: %s\n" % e)
