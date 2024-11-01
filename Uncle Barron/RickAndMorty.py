import requests

base_url = "https://rickandmortyapi.com/api/"

# Listar personajes y demas
def listar_personajes():
    response = requests.get(base_url + "character")
    data_characters = response.json()
    characters_list = []
    print("Listado de personajes en Rick & Morty:")
    
    # Ciclo for para obtener nombres de personajes en la primera página
    for index, character in enumerate(data_characters['results']):
        characters_list.append(character)
        print(f"{index + 1}. Nombre: {character['name']} - Especie: {character['species']}")
    
    # Ciclo while para recorrer todas las páginas y verlo en la lista
    next_url = data_characters['info']['next']
    while next_url:
        response = requests.get(next_url)
        data_characters = response.json()
        for character in data_characters['results']:
            characters_list.append(character)
            print(f"{len(characters_list)}. Nombre: {character['name']} - Especie: {character['species']}")
        next_url = data_characters['info']['next']
    
    return characters_list

# saber de un personaje por su namee
def mostrar_detalles_personaje_por_nombre(nombre):
    search_url = base_url + f"character/?name={nombre}"
    response = requests.get(search_url)
    data_search = response.json()

    if 'results' in data_search and data_search['results']:
        character = data_search['results'][0]
        print("\nInformación del personaje:")
        print(f"Nombre: {character['name']}")
        print(f"Especie: {character['species']}")
        print(f"Estado: {character['status']}")
        print(f"Género: {character['gender']}")
        print(f"Origen: {character['origin']['name']}")
        print(f"Ubicación actual: {character['location']['name']}")
        
        # Mostrar detalles de episodios en los que aparece
        episodios = character['episode']
        print(f"Apariciones en episodios ({len(episodios)}):")
        for episode_url in episodios:
            response_episode = requests.get(episode_url)
            data_episode = response_episode.json()
            print(f"- Episodio: {data_episode['episode']} - Título: {data_episode['name']} - Fecha de emisión: {data_episode['air_date']}")
    else:
        print("Personaje no encontrado.")

# saber ubicacioness
def listar_ubicaciones():
    response = requests.get(base_url + "location/")
    data_locations = response.json()
    print("\nListado de ubicaciones en Rick & Morty:")
    for location in data_locations['results']:
        print(f"- {location['name']} (Tipo: {location['type']}, Dimensión: {location['dimension']})")

# Lista para saber info de los episodiessss
def listar_episodios():
    response = requests.get(base_url + "episode/")
    data_episodes = response.json()
    print("\nListado de episodios de Rick & Morty:")
    for episode in data_episodes['results']:
        print(f"- {episode['episode']} - Título: {episode['name']} - Fecha de emisión: {episode['air_date']}")

print("Opciones:")
print("1. Listar personajes")
print("2. Buscar personaje por nombre")
print("3. Listar ubicaciones")
print("4. Listar episodios")

opcion = input("Seleccione una opción (1, 2, 3 o 4): ")

if opcion == '1':
    listar_personajes()
elif opcion == '2':
    nombre_personaje = input("Ingrese el nombre del personaje: ")
    mostrar_detalles_personaje_por_nombre(nombre_personaje)
elif opcion == '3':
    listar_ubicaciones()
elif opcion == '4':
    listar_episodios()
else:
    print("Opción no válida.")
