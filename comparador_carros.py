from api_key import API_KEY_CARROS
import requests

api_key = API_KEY_CARROS

url = "https://api.api-ninjas.com/v1/cars"

marca = input("Ingrese una marca: ").lower().strip()
modelo = input("\nIngrese un modelo: ").lower().strip()


headers = {
    "X-Api-Key": api_key
}

parametros = {
    "make": marca,
    "model": modelo
}


respuesta = requests.get(url, headers=headers, params = parametros)

if respuesta.status_code == 200:
    datos = respuesta.json()

    for carro in datos:
        print("Marca:", carro["make"])
        print("Modelo:", carro["model"])
        print("Año:", carro["year"])
        print("Combustible:", carro["fuel_type"])
        print("Transmisión:", carro["transmission"])
        print("-" * 30)

else:
    print("Error:", respuesta.status_code)
    print(respuesta.text)