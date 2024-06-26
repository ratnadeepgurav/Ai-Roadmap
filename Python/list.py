#Lists :- ordered and mutable :- it can be change 

lista=[1,5,6,3,7,9]

print(lista[1:4])
print(lista[::-1])
print(lista[:4:2])
print(lista[-1:-4:-1])
print(lista[2])

#List Iteration
print("\n\nFor Loop\n")

    #1 method
for i in lista:
    print(i,end=" ")

    #2 method
print("\n\nFor with range\n")
for i in range(len(lista)):
    print(lista[i],end=" ")

print("\n\nwhile loop\n")

    #3 method
i=0
while i<len(lista):
    print(lista[i],end=" ")
    i+=1
print("\n \nFor in one line\n")

[print(i,end=" ") for i in lista]

print("\n\n")

print("List Operations ")

#find length of list

len_list=len(lista)
print("Length of list is ",len_list)

#How add element in list

print(lista.append(7))

#find no occurance of char

print(lista.count(7))

#how add specific location to element

lista.insert(1,10)
print(lista)

#how remove element from list

lista.remove(3)
print(lista)

#remove element by using index number

lista.pop(1)
print(lista)


print("\n\nList Function\n\n")
#Copy function

list_copy=lista.copy()
print(list_copy)

#find index using element
print(lista.index(7))

#extend the list
c=[88,55,33]
lista.extend(c)
print(lista)

#Reverse a string
lista.reverse()
print(lista)

#Sort the string

lista.sort()
print(lista)

#clear the list

lista.clear()
print(lista)

# List 

list_a=[3,5,4,6,7]
list_b=[]

for i in list_a:
    list_b.append(list_a)
print(list_a)

#list Comprehensive

l3=[i for i in list_a if i>=4 ]
print(l3)