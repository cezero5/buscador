from duckduckgo_search import DDGS


query = ""
social_networks = []
temp_query = ""
bandera = False

num_palabra = int(input("Cuantas palabras clave deseas agregar: "))
def menu_redes():
    opcion = []
    bandera = True
    while bandera:
        print(f"1. Facebook\n2. Twitter\n3. Instagram\n4. LinkedIn\n5. TikTok\n6. Snapchat\n7. Pinterest\n8. Reddit\n9. Tumblr\n10. Youtube\n11. Otra red social\n12. Salir")
        opcion.append(int(input("Selecciona una opcion: ")))
        salir = input("Deseas agregar otra red social? (s/n): ")
        if salir == "n":
            bandera = False
    for i in opcion:
        match(i):
            case 1:
                social_networks.append("Facebook")
            case 2:
                social_networks.append("Twitter")
            case 3:
                social_networks.append("Instagram")
            case 4:
                social_networks.append("LinkedIn")
            case 5:
                social_networks.append("TikTok")
            case 6:
                social_networks.append("Snapchat")
            case 7:
                social_networks.append("Pinterest")
            case 8:
                social_networks.append("Reddit")
            case 9:
                social_networks.append("Tumblr")
            case 10:
                social_networks.append("Youtube")
            case 11:
                social_networks.append(input("Nombre de la red social: "))
            case _:
                print("Opcion no valida")

def linea_busqueda():
    
    nombre = input("A quien buscaremos hoy: ")
    imagen = input("Deseas buscar imagenes de esta persona? (s/n): ")  
    for i in social_networks:
        query = f"{i} de {nombre} AND {temp_query}"
        search_results(query)

        img_search_s_n(imagen)
        img_search(query)

def search_results(query):
        
        search_results = DDGS().text(query, max_results=2, region="us-en", safesearch="off")
        
        print("Busqueda de paginas web")
        for result in search_results:
            print(f"{result["title"]}\n {result["href"]}\n {result["body"]}\n\n")

def img_search_s_n(imagen):    
    bandera = False

    if imagen == "s":
        bandera = True
    
    elif imagen == "n":
        print("Saliendo...")
        bandera = False

    return bandera

def img_search(query):
    print("\nBusqueda de imagenes")
    search_image = DDGS().images(query, max_results=2, region="us-en", safesearch="off")
    for img in search_image:
        print(f"{img["title"]} \n {img["image"]}\n\n")



def palabra_clave(num_palabra):
    count_palabra = ""
    while(num_palabra > 0):
        palabra = input("Palabra clave: ")
        count_palabra += f"{palabra} AND "
        num_palabra -= 1
    return count_palabra


def query_search(num_palabra):
    global temp_query
    if(num_palabra > 0):
        temp_query = palabra_clave(num_palabra)
    return str(temp_query)

menu_redes()
query_search(num_palabra)
linea_busqueda()