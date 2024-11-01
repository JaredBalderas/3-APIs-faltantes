import requests

base_url = "https://swapi.dev/api/"

# hacer lista para ver los campos
def listar_personajes():
    response = requests.get(base_url + "people/")
    data_people = response.json()
    characters_list = []
    print("Listado de personajes en Star Wars:")
    
    for index, character in enumerate(data_people['results']):
        characters_list.append(character)
        print(f"{index + 1}. Nombre: {character['name']} - Altura: {character['height']} cm")
    
    
    next_url = data_people['next']
    while next_url:
        response = requests.get(next_url)
        data_people = response.json()
        for character in data_people['results']:
            characters_list.append(character)
            print(f"{len(characters_list)}. Nombre: {character['name']} - Altura: {character['height']} cm")
        next_url = data_people['next']
    
    return characters_list

# Mostrar info de un personajee por su nombre
def mostrar_detalles_personaje_por_nombre(nombre):
    search_url = base_url + f"people/?search={nombre}"
    response = requests.get(search_url)
    data_search = response.json()

    if data_search['results']:
        character = data_search['results'][0]
        print("\nInformacion del personaje:")
        print(f"Nombre: {character['name']}")
        print(f"Altura: {character['height']} cm")
        print(f"Ano de nacimiento: {character['birth_year']}")
        print(f"Genero: {character['gender']}")
        print(f"Color de ojos: {character['eye_color']}")
        print(f"Color de piel: {character['skin_color']}")
        print(f"Peso: {character['mass']} kg")

        
        peliculas = character['films']
        print(f"Apariciones en peliculas ({len(peliculas)}):")
        for film_url in peliculas:
            response_film = requests.get(film_url)
            data_film = response_film.json()
            print(f"- Titulo: {data_film['title']} - Episodio: {data_film['episode_id']} - Fecha de lanzamiento: {data_film['release_date']}")
    else:
        print("Personaje no encontrado.")

# Obtener informacino en genereal de las moviess y demas
def detalles_peliculas():
    response = requests.get(base_url + "films/")
    data_films = response.json()
    print("\nInformacion sobre las peliculas de Star Wars:")
    print(f"Numero total de sagas: {len(data_films['results'])}")
    for film in data_films['results']:
        print(f"- Titulo: {film['title']} - Episodio: {film['episode_id']} - Fecha de lanzamiento: {film['release_date']}")

# Menu principal
print("Opciones:")
print("1. Listar personajes")
print("2. Buscar personaje por nombre")
print("3. Ver detalles de peliculas")

opcion = input("Seleccione una opcion (1, 2 o 3): ")

if opcion == '1':
    listar_personajes()
elif opcion == '2':
    nombre_personaje = input("Ingrese el nombre del personaje: ")
    mostrar_detalles_personaje_por_nombre(nombre_personaje)
elif opcion == '3':
    detalles_peliculas()
else:
    print("Opcion no valida.")
