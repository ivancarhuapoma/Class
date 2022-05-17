#practices with find,count,split...
def getseparador():
    return print('Nueva funcion : ')


imail = 'ivan santos carhuapoma mezarina'
#find ---> 0,1,2..
fi = imail.find('carhuapoma')
print(fi ,'\n')

#count
getseparador()
con = imail.count('a')
print(con)

#split
getseparador()
fr = imail.split()
print(fr)
#print(type(fr)) --->se convierte en lista

    # METODOS DE LISTAS
mylist = ['ivan',24,'agosto',True,'agosto']

#append
getseparador()
mylist.append('gino')
print(mylist)
#insert    ---> 1,2,3,...
getseparador()
mylist.insert(2,'Vanessa')
print(mylist)

#remove
getseparador()
mylist.remove('agosto')
print(mylist)

#pop ---> delete last elemente 
# tambein si le indicamos el indice del elemento lo elimina
getseparador()
newlist = ['enero','febrero','marzo','abril']
print(newlist)
last = newlist.pop()
print(last)     


#sort  --> ordena de forma ascendente
getseparador()
listnew = [1023,21,31,400,54,4,23,8]
listnew.sort()
print(listnew)
#al reves = descendente
listnew.sort(reverse=True)
print(listnew)

# reverse() 
l = [1, 2, 3]
l.reverse()
print(l) #[3, 2, 1]

#extend -->
getseparador()
li = [1,65,44,2222,800]
li2 = [33,77]
li.extend(li2)
print(li)

#append -->muy diferente a extend
li.append(li2)
getseparador()   
print(li)

