"""
Ejemplo vanilla: Gemini API con requests
Para probar la capa gratuita antes de decidir si se usa en clase.

A diferencia de PokeAPI, esta API si pide autenticacion. Para conseguir
una API key gratuita (sin tarjeta):

1. Entrar a https://aistudio.google.com
2. Iniciar sesion con una cuenta de Google normal
3. Click en "Get API key" y copiar la key que genera

Documentacion oficial: https://ai.google.dev/gemini-api/docs
"""
from api_key import API_KEY
import requests

#CONSTANTES 
VERBOSE = False
MODEL = "gemini-3.6-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"


if VERBOSE:
    print(f"/n ====================" )
    print(f"GEMINI MODEL : {MODEL}")
    print(f"API KEY: {API_KEY}")
    print(f"/n ====================" )

# A diferencia de PokeAPI, aqui la key no va en la URL: va en un header.
# Poner credenciales en la URL es mala practica (queda en logs, historial
# del navegador, etc.), asi que Gemini pide mandarla en un header aparte.
headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY,
}

#menu para preguntar

while True:

    print(f"\n============== Gemini ==============")

    user_prompt = input("¿En qué piensas? (ingresa tu prompt o salir para terminar la sesión): ")

    if user_prompt.strip().lower() == "salir":
        print("\nHasta luego!")
        break

    body = {
        "contents": [
            {
                "parts": [
                    {"text": user_prompt}
                ]
            }
        ]
    }

    respuesta = requests.post(URL, headers=headers, json=body)

    print("Status code:", respuesta.status_code)

    if respuesta.status_code != 200:
        print("Algo salió mal:")
        print(respuesta.text)
    else:
        datos = respuesta.json()

        texto = datos["candidates"][0]["content"]["parts"][0]["text"]

        print("\nRespuesta de Gemini:\n")
        print(texto)


