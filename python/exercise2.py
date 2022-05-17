#Definir una función superposicion() que tome dos
#  listas y devuelva True si tienen al menos 1 
# miembro en común o devuelva False de lo 
# contrario. Escribir la función usando el
#  bucle for anidado.


#Primera forma 
def getwords(li1,li2):
    for i in li1:
        for j in li2:
            if i == j:
                return True
            else:
                continue
    return False

lista1 = ['i', 'j', 'k', 'l']
lista2 = ['a', 'e', 'r', 'i']

#Segunda forma
def getword2(a,b):
    for i in a:
        if i in b:
            return True
    return False

print(getword2(lista1,lista2))