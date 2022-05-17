    #METODOS DE DICCIONARIOS

def otherfuncion():
    return print('\notro motodo')

#get() -->busca un elemento apartir  de su clave
        # si no lo encuentra devuelve el otro valor
colores = { "amarillo":"patito", 
            "azul":"cielo", 
            "verde":"green" }

valor = colores.get('verde','NO ENCONTRO')
print(valor)

#keys() --->genera una lista en clave de los llaves del diccionario
otherfuncion()
li=colores.keys()
print(li)

#values() genera un alista con los valores del diccionario
otherfuncion()
fr = colores.values()
print(fr)

#items() Genera una lista con los elementos del diccionario(clave-vaalor)
otherfuncion()
ty = colores.items()
print(ty)
for y,v in colores.items():
    print(y,v)

#pop() -->Extrae un valor apartir de su clave y lo elimina
otherfuncion()
print(colores)
rr=colores.pop('azul','NO ENCONTRE ...')
print(rr)
print(colores)

#clear() -->borra todos los registros de un diccionario
otherfuncion()
colores.clear()
print(colores)





