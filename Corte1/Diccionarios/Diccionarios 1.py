#sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22} 
#guardar pares clave–valor
# num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}
#guarda la cantidad de cámaras en distintos lugares.
# print(sensors)
# imprimir en pantalla todo el diccionario sensors.
# print(num_cameras)
#imprime el diccionario num_cameras

# translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
#mini diccionario de traducciones
# print(translations)
# imprimo las traducciones

##Verifiying an error:
#Es solo un comentario (no se ejecuta). Sirve para que recuerdes que estás probando un error.
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
#claves son listas, y eso genera un error (TypeError: unhashable type: 'list') porque las listas no pueden ser claves de un diccionario.
# # print(powers)
#imprimir el diccionario powers

# children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
# Apellido, hijos 
# print(children)
#muestra todo el diccionario de una sola vez en su formato interno.

# my_empty_dictionary = {}
#crea un diccionario vacío, sin claves ni valores dentro.
# print(my_empty_dictionary)
#muestra su contenido en pantalla.

# menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
#Crea un diccionario con platos y precios.
# print("Before: ", menu)
#Imprime el menu
# menu["cheesecake"] = 8
#Se agrega "cheesecake": 8 al diccionario.
# print("After", menu)
#Imprime el menu con los cambios
# animals_in_zoo = {"dinosaurs": 0}
#Primero se crea con
# animals_in_zoo = {"dinosaurs": 0}
#vuelve a poner lo mismo (no cambia nada).
# animals_in_zoo = {"horses": 2}
#lo sobrescribe completamente con {"horses": 2}.
# print(animals_in_zoo)
#imprime 

# #If we wanted to add 3 new rooms, we could use:
#
# sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
#se añaden tres nuevas claves con sus valores
# print("After", sensors)
# imrpime despues

# user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
# Le asigna a una variable un diccionario con dos pares clave–valor:
# print(user_ids)
# Imprime el contenido actual del diccionario en pantalla.
# user_ids.update({"theLooper": 138475, "stringQueen": 85739})
# Agrega dos nuevas claves con sus valores al diccionario usando .update().
# print(user_ids)
# Imprime el diccionario después de la actualización, mostrando las nuevas claves añadidas.

## Overwrite Values ##
# Título o comentario general: vamos a ver cómo sobrescribir valores en un diccionario.
# We know that we can add a key by using the following syntax:
# Comentario explicativo: recuerda que podemos agregar una clave con la sintaxis diccionario["clave"] = valor.
# menu["banana"] = 3
# Ejemplo de cómo se agregaría una nueva clave "banana" con valor 3 (si existiera la variable menu).
# menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
# Crea un diccionario llamado menu con cuatro pares clave–valor.
# print("Before: ", menu)
# Imprime el diccionario antes de cambiar nada.
# menu["oatmeal"] = 5
# Sobrescribe el valor de la clave "oatmeal": antes era 3, ahora pasa a ser 5.
# print("After", menu)
# Imprime el diccionario después de la modificación, mostrando el nuevo valor de "oatmeal".

## Notice the value of "oatmeal" has now changed to 5.
# oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
# Le asigna a la variable `oscar_winners` un diccionario con categorías de los Óscar y sus ganadores.
# print("Before", oscar_winners)
# Imprime el texto "Before" seguido del contenido inicial del diccionario.
# print()
# Imprime una línea en blanco para separar visualmente las salidas.
# oscar_winners.update({"Supporting Actress": "Viola Davis"})
# Agrega un nuevo par clave–valor al diccionario, donde la clave es "Supporting Actress" y el valor es "Viola Davis".
# print("After1", oscar_winners)
# Imprime el texto "After1" seguido del diccionario actualizado con la nueva clave–valor.
# print()
# Imprime otra línea en blanco para separar la salida.
# oscar_winners["Best Picture"] = "Moonlight"
# Modifica el valor de la clave "Best Picture", que antes era "La La Land", y ahora se sobrescribe con "Moonlight".
# print("After2", oscar_winners)
# Imprime el texto "After2" seguido del diccionario ya modificado.

###Dict Comprehensions
#Let’s say we have two lists that we want to combine into a 
#dictionary, like a list of students and a list of their heights, 
#in inches:

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
# Se crea una lista con nombres de estudiantes.

heights = [61, 70, 67, 64]
# Se crea una lista con las alturas correspondientes a cada estudiante.

#Python allows you to create a dictionary using 
# a dict comprehension, with this syntax:

# zipStudents = zip(names, heights)
# Une las dos listas en pares (tuplas) de elementos correspondientes.
# Resultado: [("Jenny", 61), ("Alexus", 70), ("Sam", 67), ("Grace", 64)] (aunque zip devuelve un objeto iterable).

# print("zipStudents: ", zipStudents)
# Imprime el objeto `zip` (mostrará algo como <zip object at ...>).

# students = {key:value for key, value in zip(names, heights)}
# Crea un diccionario usando comprensión de diccionarios.
# Resultado: {"Jenny": 61, "Alexus": 70, "Sam": 67, "Grace": 64}

# print(students)
# Imprime el diccionario con cada estudiante y su altura.

# #zip() combines two lists into an iterator of tuples with the list elements paired together. This dict comprehension:

# drinks = ["espresso", "chai", "decaf", "drip"]
# Se crea una lista con nombres de bebidas.

# caffeine = [64, 40, 0, 120]
# Se crea una lista con la cantidad de cafeína de cada bebida.

# zipped_drinks = zip(drinks, caffeine)
# Une las dos listas en pares (bebida, cantidad de cafeína).

# print(zipped_drinks)
# Imprime el objeto `zip` (otra vez algo como <zip object at ...>).

# drinks_to_caffeine = {key:value for key, value in zipped_drinks}
# Convierte el resultado de zip en un diccionario.
# Resultado: {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

# print(drinks_to_caffeine)
# Imprime el diccionario de bebidas y cafeína.

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
# Lista con títulos de canciones.

playcounts = [78, 29, 44, 21, 89, 5]
# Lista con el número de veces que cada canción ha sido reproducida.

plays = {key:value for key, value in zip(songs, playcounts)}
# Une las dos listas y crea un diccionario {canción: número de reproducciones}.
# Resultado inicial: {"Like a Rolling Stone": 78, "Satisfaction": 29, ...}

print(plays)
# Imprime el diccionario de canciones con sus reproducciones.

plays.update({"Purple Haze": 1})
# Agrega una nueva canción "Purple Haze" con 1 reproducción al diccionario.

plays.update({"Respect": 94})
# Actualiza la canción "Respect", que tenía 89 reproducciones, a 94.

print("After: ", plays)
# I
