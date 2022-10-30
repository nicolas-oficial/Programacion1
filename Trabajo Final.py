  # Nicolás Oficialdegui.    Programación 1. 

cancion1 = {"titulo": 'La yapa', "artista": 'Los Nocheros', "letra": 'una joya para mi es el sabor de tus besos, se caen del propio peso...'}
cancion2 = {"titulo": 'Bombon asesino', "artista": 'Los Palmeras', "letra": 'es que ella tiene un bombón asesino, se sabe un bombón bien latino...'}
cancion3 = {"titulo": 'A mi manera', "artista": 'Cacho Castaña', "letra": 'estoy mirando atras y puedo ver mi vida entera y se que estoy en paz, pues la viví a mi manera'}
cancion4 = {"titulo": 'Ojala que no puedas', "artista": 'Cacho Castaña', "letra": 'ojalá que no puedas ni besarla en la boca y al mirarla a los ojos...'}
cancion5 = {"titulo": 'El duende del bandoneon', "artista": 'Soledad', "letra": 'comienza a pechar la gente al llegar porque el baile ya empezó...'}

listaCanciones = [cancion1, cancion2, cancion3, cancion4, cancion5]

#-------------------------------------------------------------------------------------------------------------
def buscarCancion():            # Buscar canción
    title = input('Ingrese el nombre de la canción que desea buscar: ')
    for cancion in listaCanciones:
        if title == cancion["titulo"]:
            print('La canción fue encontrada en la lista.')
            print('Titulo:',cancion["titulo"])
            print('Artista:',cancion["artista"])
            print('Letra:',cancion["letra"])
        else:
            print('La canción que busca No está en la lista.')
   
#-----------------------------------------------------------------------------------
                    
def agregarCancion():                        # Agregar canción 
    title = input('Ingrese el título de la nueva canción: ')
    artist = input('Ingrese el artista: ') 
    words = input('Ingrese la letra de la canción: ')
    cancion = {"titulo": title, "artista": artist, "letra": words}
    listaCanciones.append(cancion)

#------------------------------------------------------------------------------------

def modificarCancion():        # Modificar una canción 
    
    title = input('Ingrese el nombre de la canción que desea modificar: ')
    for cancion in listaCanciones:
        if title == cancion["titulo"]:
            print('La canción fue encontrada en la lista.')
            print('Titulo:',cancion["titulo"])
            print('Artista:',cancion["artista"])
            print('Letra:',cancion["letra"])

            nuevoTitulo = input('Ingrese el nuevo titulo de la canción: ')
            cancion['titulo'] = nuevoTitulo 
            nuevoArtista = input('Ingrese el nuevo artista: ')
            cancion['artista'] = nuevoArtista
            nuevaLetra = input('Ingrese la nueva letra de la canción: ') 
            cancion['letra'] = nuevaLetra

print('===============================================================')
print('         Bienvenido al gestor de canciones.') 
print('===============================================================')    
print('Presione 1 para ver la lista de canciones.')
print('Presione 2 para almacenar nueva canción.')
print('Presione 3 para buscar una determinada canción por su nombre.')
print('Presione 4 para modificar una canción.')
print('Presione 0 para salir de programa.')
print('===============================================================') 

opcion = int(input('Ingrese una opción 1 - 2 - 3 - 4 o 0: ')) 

while opcion != 0:          
           
    if opcion == 1:
        for i in listaCanciones:
            print(i)
    elif opcion == 2:
        agregarCancion()
        for lista in listaCanciones:
            print(lista)
    elif opcion == 3:
        buscarCancion()
    elif opcion == 4:
        modificarCancion()
        for i in listaCanciones:
            print(i)
    else:
        print('Ingrese una opción correcta.')

    opcion = int(input('Ingrese una opción 1 - 2 - 3 - 4 o 0: '))
  
print('Usted finalizó el administrador de canciones.')