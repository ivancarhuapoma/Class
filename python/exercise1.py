#Define una funcion que reciba una frase y retorne True si es palindroma
#en caso contrario False

#Funcion para frases palindromas
def getpalindromo(var):
    var = var.replace(' ','')
    bol = var[::-1]
    if var == bol:
        return True
    else:
        return False
    
#funcion solo para palabras palindromas
def justwordspalindromas(rf):
    gg=rf[::-1]
    if gg == rf:
        return True
    else:
        return False

word = input('Ingresa una frase palindroma: ')
print(justwordspalindromas(word))