#list Problem Solving

l1=["Ross","Rachel","Monica","Joe"]

#swap from 1st element to last element
l1[0],l1[3]=l1[3],l1[0]
print(l1)

#Add new value in 2nd position

l1.insert(2,"Ratnadeep")
print(l1)

#Delete value for 3rd postion
l1.pop(2)
print(l1)

#mulitiply all list element

l2=[8,5,9,3,5,1]
a=1
for i in l2:
    a*=i
print(a)

#Largest number from list

l2.sort()
print(l2[-1])