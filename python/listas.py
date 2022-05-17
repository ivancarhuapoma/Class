        #LISTAS
#son mutables(sus elementos pueden ser modificados
#son dinamicas(se puede añadir o eliminar elementos
#Los 2 anteriores las diferencia con las tuplas y los sets
#Son ordenadas, mantienen el orden de su creacion
#Pueden ser indexadas con [i]
#Se pueden anidar, o sea meter una dentro de otra
#La posicion va desde 0,1,2,3..

#Crear listas
lista = [1,2,3,4,5,6,7,8]

#Tambien desde otro objeto usando list(solo en objetos iterables)
li = (15,3) #<---tupla
print(type(li))
li = list(li) #cambiamos a tupla en lista
print(li)
print(type(li))

#Se pueden almacenar diferentes tipos de datos
rt = [1,'ivan',3,True,53,'leo',7]

#Acceso a las listas
e = ['ivan',33,True]
print(e[0]) #'ivan'
print(e[1]) #33
#para acceder al ultimo elemento
print(e[-1]) #True

#Para modificar algun elemento 
    # con asignacion
e[2] = 'Goku'
print(e) #['ivan', 33, 'Goku']
    #con del 
del e[1] 
print(e) #['ivan', 'Goku']

#listas de listas 
x = [1, 2, 3, ['p', 'q', [5, 6, 7]]]
print(x[3][0])    #p
print(x[3][2][0]) #5
print(x[3][2][2]) #7

#Sublistas de una listas
l = [1, 2, 3, 4, 5, 6]
print(l[0:2]) #[1, 2]
print(l[2:6]) #[3, 4, 5, 6]

#modificar multiples valores uasndo :
l = [1, 2, 3, 4, 5, 6]
l[0:3] = [0, 0, 0]
print(l) #[0, 0, 0, 4, 5, 6]

#uso del + en listas
l = [1, 2, 3]
l += [4, 5]
print(l) #[1, 2, 3, 4, 5]

#algo curioso OBSERBAR :O
listaa = [1, 2, 3]
x, y, z = listaa
print(x, y, z) #1 2 3

#ITERAR LISTAS
lista = [5, 9, 10]
for l in lista:
    print(l)
#5
#9
#10

#Si necesitamos un índice acompañado con la lista
#enumerate te devuelve los elementos con su posicion
lista = [5, 9, 10]
for index, l in enumerate(lista):
    print(index, l)
#0 5
#1 9
#2 10

#si tenemos dos listas y las queremos iterar a la vez, 
# también es posible hacerlo

lista1 = [5, 9, 10]
lista2 = ["Jazz", "Rock", "Djent"]
for l1, l2 in zip(lista1, lista2):
    print(l1, l2)
#5 Jazz
#9 Rock
#10 Djent

#haciendo uso de len()
lista1 = [5, 9, 10]
for i in range(0, len(lista)):
    print(lista1[i])
#5
#9
#10


#LOS METODOS DE LAS LISTAS LOS ENCONTRAMOS EN 1.py


