from api_key import API_KEY_CARROS
import requests

api_key = API_KEY_CARROS

url = "https://api.api-ninjas.com/v1/cars"

marca = input("Ingrese una marca: ").lower().strip()
modelo = input("Ingrese un modelo: ").lower().strip()


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
        for carro in datos:
                print("Marca:", carro.get("make", "No disponible"))
                print("Modelo:", carro.get("model", "No disponible"))
                print("Año:", carro.get("year", "No disponible"))
                print("Combustible:", carro.get("fuel_type", "No disponible"))
                print("Transmisión:", carro.get("transmission", "No disponible"))
                print("Sistema de tracción:", carro.get("drive", "No disponible"))
                print("Cilindros:", carro.get("cylinders", "No disponible"))
                print("Clase:", carro.get("class", "No disponible"))
                print("-" * 30)

else:
    print("Error:", respuesta.status_code)
    print(respuesta.text)