# adding data in list 

fruit =[]
f1=input("Enter frinds name")
fruit.append(f1)
f2=input("Enter frinds name")
fruit.append(f2)
f3=input("Enter frinds name")
fruit.append(f3)
f4=input("Enter frinds name")
fruit.append(f4)
f5=input("Enter frinds name")
fruit.append(f5)

print(fruit)

#getting 6 student marks and arrenagd it in sorted order

marks=[]
a=int(input("Enter a marks"))
marks.append(a)

b=int(input("Enter a marks"))
marks.append(b)

c=int(input("Enter a marks"))
marks.append(c)

d=int(input("Enter a marks"))
marks.append(d)

e=int(input("Enter a marks"))
marks.append(e)

marks.sort()
print(marks)

#Sum a list with 4 numbers


l=[33,55,22,11]
a=0
for i in range(0,len(l)):
    a=a+l[i]
print(a)

#or use -->print(sum(l))


#count the number from following tuple

a=(7,6,4,6,7,2,2)

count_tuple=a.count(2)
print(count_tuple)



