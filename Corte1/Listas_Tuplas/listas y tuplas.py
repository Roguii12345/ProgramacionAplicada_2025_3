my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
# Se crea una lista con 6 colores.

print(my_lista)
# Muestra la lista completa.

print(type(my_lista))
# Imprime el tipo → <class 'list'>.

print(my_lista[2])
# Accede al índice 2 → "Amarillo".

print("my_lista size: ", len(my_lista))
# len() devuelve el tamaño de la lista → 6.

print(my_lista[0:2])
# Slice: devuelve elementos desde índice 0 hasta 1 → ['Rojo', 'Azul'].

print(my_lista[:2])
# Equivalente, ya que omitir el 0 empieza desde el principio.

my_lista.append('Blanco')
# Agrega "Blanco" al final de la lista.

my_lista.insert(3, 'Negro')
# Inserta "Negro" en el índice 3 (entre "Amarillo" y "Naranja").

my_lista.extend(['Marron', 'Gris'])
# Agrega dos elementos más al final de la lista.

print(my_lista.index('Azul'))
# Busca el índice de "Azul" → 1.

# my_lista.remove('Magenta')   # Daría error porque no existe.
my_lista.remove('Marron')
# Elimina la primera aparición de "Marron".

my_lista.insert(8, 'Marron')
# Inserta "Marron" en la posición 8.

print(my_lista.pop())
# pop() quita y devuelve el último elemento → "Gris".

size = len(my_lista)
print("size = ", size)
# Muestra el tamaño actual de la lista.

my_lista_3 = my_lista * 3
print("my_lista_3: ", my_lista_3)
# Multiplica la lista por 3 → la repite tres veces concatenada.

print("Sort:")
my_listaSort = my_lista.sort()
print(my_listaSort)
# .sort() ordena la lista pero devuelve None.
# Para verla ordenada hay que imprimir my_lista directamente.

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordering my_NumList: ")
my_NumList.sort()
print(my_NumList)
# Ordena la lista de menor a mayor.

my_NumList.sort(reverse = True)
print("De menor a mayor: ", my_NumList)
# Ordena de mayor a menor porque reverse=True.

print("############TUPLAS#########")

my_tupla = tuple(my_lista)
# Convierte la lista en tupla (inmutable).

print(my_tupla[0])  # Primer elemento
print(my_tupla[2])  # Tercer elemento

print('Rojo' in my_tupla)
# Verifica si "Rojo" está dentro de la tupla → True.

print(my_tupla.count('Rojo'))
# Cuenta cuántas veces aparece "Rojo".

my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)
# CUIDADO: esto no es una tupla, es un string.
# Una tupla de un solo elemento debe escribirse ('Blanco',).

my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)
# Empaquetado de tupla: se crea sin paréntesis.

nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)
# Desempaquetado: cada variable toma un valor en orden.

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)
# Muestra todos los valores de manera organizada.

my_lista2 = list(my_tupla)
print(my_lista2)
# Convierte la tupla en lista (mutable).
