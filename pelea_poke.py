from random import choice
from time import sleep

def waiting():
    print('\n...')
    sleep(0.5)

def print_bonito(pokemon):
    return(f'{pokemon["nombre"]} (HP: {pokemon["hp"]} | AD: {pokemon["ad"]})')

def damage(pokemon, ad):
    pokemon["hp"] = pokemon["hp"] - ad
    

def attack(atacante, rival):

        if atacante["tipo"] == 'electrico':
            ataque = 'Impactrueno'
        elif atacante["tipo"] == 'planta':
            ataque = 'Hoja navaja'
        elif atacante["tipo"] == 'fuego':
            ataque = 'Llamarada'
        else:
            ataque = 'Cañon de agua'   

        damage(rival, atacante["ad"])

        print(f'\n({atacante["nombre"]}) Ataca con {ataque} | -{atacante["ad"]}')



pokemones = {
    "pikachu":{
        "nombre": "Pikachu",
        "tipo": "electrico",
        "hp": 60,
        "ad": 15
    },

    "chikorita":{
            "nombre": "Chikorita",
            "tipo": "planta",
            "hp": 45,
            "ad": 10
    },

    "charmander":{
                "nombre": "Charmander",
                "tipo": "fuego",
                "hp": 40,
                "ad": 10
        },

    "froakie":{
                "nombre": "Froakie",
                "tipo": "agua",
                "hp": 40,
                "ad": 20
        }
}

pokemones_posibles = list(pokemones.values())

pokemon_1 = choice(pokemones_posibles).copy()
pokemon_2 = choice(pokemones_posibles).copy()



print('\n ------ POKEMON SELECCIONADOS ------')

waiting()
print(f"\nPokemon 1: {print_bonito(pokemon_1)}")
print(f"Pokemon 2: {print_bonito(pokemon_2)}")

while True:

    waiting()
    attack(pokemon_1, pokemon_2)

    if pokemon_2["hp"] <= 0:
        print(f"\nGAME OVER: {pokemon_1["nombre"]} venció a {pokemon_2["nombre"]}")
        break

    waiting()
    attack(pokemon_2, pokemon_1)
    
    if pokemon_1["hp"] <= 0:
        print(f"\nGAME OVER: {pokemon_2["nombre"]} venció a {pokemon_1["nombre"]}")
        break

    waiting()
    print("\nHPs restantes")
    print(f"{pokemon_1["nombre"]}: {pokemon_1["hp"]}")
    print(f"{pokemon_2["nombre"]}: {pokemon_2["hp"]}")      

    







