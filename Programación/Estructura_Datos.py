'''
Las estructuras de datos en Python son maneras de organizar y almacenar datos para permitir un acceso y 
una manipulación eficientes dentro de un programa.
'''

#TUPLAS:
#las tuplas son conjuntos de datos que no se pueden modificar despues de su creación.
#la ventaja de estas es que optimizan el codigo al ser inmutables.

primera_tupla = ('elemento0','elemento1','elemento3')

print(primera_tupla)

#algunos operaciones para tuplas:

a = primera_tupla[0] #Los indices en python incian en cero

print(a)

print(len(primera_tupla)) #longitud de la tupla

print(primera_tupla.index('elemento3')) #Nos dice en donde esta un elemento de la tupla

segunda_tupla = (1,2,3)

print(primera_tupla+segunda_tupla) # + concatena las tuplas

#LISTAS:

primera_lista = list(primera_tupla) #podemos convertir una tupla a una lista

primera_lista.append(8) #agregamos un elemento en la ultima posición

print(primera_lista)

primera_lista.insert(2,'agregué un elemento') #Podemos agregar un elemento en un indice a elección
