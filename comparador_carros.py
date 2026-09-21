from api_key import API_KEY_CARROS
import requests

api_key = API_KEY_CARROS

url = "https://api.api-ninjas.com/v1/cars"

def buscar_carros():
    marca = input("\nIngrese una marca: ").lower().strip()
    modelo = input("Ingrese un modelo: ").lower().strip()
    año = int(input("Ingrese el año del modelo: "))
    print("\n")


    headers = {
        "X-Api-Key": api_key
    }

    parametros = {
        "make": marca,
        "model": modelo,
        "year": año
    }


    respuesta = requests.get(url, headers=headers, params = parametros)

    if respuesta.status_code == 200:
        datos = respuesta.json()

        if len(datos) == 0:
             print("No se encontro informacion de esa marca o modelo...\n")

        else:
            for carro in datos:
                    print("Marca:", carro.get("make", "No disponible"))
                    print("Modelo:", carro.get("model", "No disponible"))
                    print("Combustible:", carro.get("fuel_type", "No disponible"))
                    print("Transmisión:", carro.get("transmission", "No disponible"))
                    print("Sistema de tracción:", carro.get("drive", "No disponible"))
                    print("Cilindros:", carro.get("cylinders", "No disponible"))
                    print("Clase:", carro.get("class", "No disponible"))
                    print("-" * 30)

    else:
        print("Error:", respuesta.status_code)
        print(respuesta.text)

def menu():
     opcion = ""

     while opcion != "2":
          
        print("========== BusCAR ==========")
        print("1. Buscar carro")
        print("2. Salir")
        print("==========================")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            buscar_carros()

        elif opcion == "2":
            print("\nSaliendo...")

        else:
            print("\nOpción inválida...\n")

menu()