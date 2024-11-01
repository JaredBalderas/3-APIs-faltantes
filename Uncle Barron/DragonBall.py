import requests
import json

# URL base de la API
base_url = "https://dragonball-api.com/api/"

# Función para listar personajes
def listar_personajes():
    response = requests.get(base_url + "characters", verify=False)  # Ignorar verificación SSL
    if response.status_code == 200:
        data_characters = response.json()
        print("\nListado de personajes de Dragon Ball Super:")
        for character in data_characters['items']:
            print(f"Nombre: {character['name']} - Raza: {character['race']}")
    else:
        print("Error al listar personajes:", response.status_code)

# Función para buscar personaje por ID
def buscar_personaje_por_id(id_personaje):
    response = requests.get(base_url + f"characters/{id_personaje}", verify=False)  # Ignorar verificación SSL
    if response.status_code == 200:
        data_character = response.json()
        print(f"\nResultados de búsqueda para el ID '{id_personaje}':")
        print(f"Nombre: {data_character['name']} - Género: {data_character['gender']} - Raza: {data_character['race']}")
    else:
        print(f"Error al buscar el personaje: {response.status_code} Client Error: Not Found for ID {id_personaje}")

# Función para listar planetas
def listar_planetas():
    response = requests.get(base_url + "planets", verify=False)  # Ignorar verificación SSL
    if response.status_code == 200:
        data_planets = response.json()
        print("\nListado de planetas en Dragon Ball Super:")
        for planet in data_planets['items']:
            print(f"Nombre: {planet['name']} - Dimensión: {planet.get('dimension', 'Desconocida')}")
    else:
        print("Error al listar planetas:", response.status_code)

# Función para listar planetas destruidos
def filtrar_planetas_destruidos():
    response = requests.get(base_url + "planets?isDestroyed=true", verify=False)  # Ignorar verificación SSL
    if response.status_code == 200:
        data_planets = response.json()
        print("\nListado de planetas destruidos:")
        if isinstance(data_planets, list):
            for planet in data_planets:
                print(f"- {planet['name']} (ID: {planet['id']})")
        else:
            for planet in data_planets['items']:
                print(f"- {planet['name']} (ID: {planet['id']})")
    else:
        print("Error al listar planetas destruidos:", response.status_code)

# Menú principal
def main():
    while True:
        print("\nOpciones:")
        print("1. Listar personajes")
        print("2. Buscar personaje por ID")
        print("3. Listar planetas")
        print("4. Listar planetas destruidos")
        
        opcion = input("Seleccione una opción (1, 2, 3 o 4): ")
        
        if opcion == '1':
            listar_personajes()
        elif opcion == '2':
            id_personaje = input("Ingrese el ID del personaje que desea buscar: ")
            buscar_personaje_por_id(id_personaje)
        elif opcion == '3':
            listar_planetas()
        elif opcion == '4':
            filtrar_planetas_destruidos()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            continue

# Ejecutar el menú principal
main()
