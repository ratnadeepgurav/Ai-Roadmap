#access dictionary data

dictionary={"name":"Ratnadeep","Villege":"Kolhapur","Age":20}
print(dictionary["name"],["Villege"])

#Iteration of dictionary

for d in dictionary:
    print(dictionary[d])#for accessing the values 
   #print(d)for accessing only the keys
    
for j in dictionary.values():#acees value using values() function
    print(j)

#display both keys and values using items function
for i,j in dictionary.items():
    print(i,":",j)    

#dictionary function
    
    #get() :-  Return an value 
fetch=dictionary.get("name")
print(fetch)

    #items() :- return the keys and values in tuple form
ita=dictionary.items()
print(ita)

    #keys():-  return the keys of dictionary
key=dictionary.keys()
print(key)
    
    #values() :-  return the values of dictionary
val=dictionary.values()
print(dictionary.values())

    #copy() :- copy dictionary 

cp=dictionary.copy()
print(cp)

    #setdefault() :- set default value for dictionary 
df=dictionary.setdefault("Name","Ratna")
print(df)

dict1={1:{"name":"Ratnadeep","Age":19},
2:{"name":"Pranav","Age":20},
3:{"name":"Ritesh","Age":26}}

print(dict1[3]["Age"])
print(dict1)



#Problem solving

    #problem 1:- sort dictinary value 

dict2={"age":2,"gae":4,"eag":5,"dea":5}
print(sorted(dict2.values()))

    #problem 2 :- keys are number from 1 to 15 and values are square root of this keys
dict3={}
for i in range(1,16):
    dict3[i]=i**2
print(dict3)

    #problem 3 :- multiplication of value

product=1
for i in dict2:
    product=product*dict2[i]
print(product)

    #problem 4 :- sort the values of dictionary

print(sorted(dict2.values()))