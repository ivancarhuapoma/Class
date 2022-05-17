#Calcular el ind.masa.cop

#Funcion de ind.masa.cop
def masacor():
    while True:
        w= int(input('ingrese su peso : '))
        h= float(input('ingrese su altura : '))
        masa=0
        if h==0 or w==0:
            print ("Por favor ingrese datos correctos.")
            continue
        else:
            masa=w/h
            #masa= str(masa)
            break
    return masa

print(masacor())

