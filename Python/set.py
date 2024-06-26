#sets :- remove duplicate element

a={"fd","fd","rth","sll"}
print(a)

for i in a:
    print(i)

#set function
    
a.add("hello")
print(a)

a.pop()
print(a)

a.discard("hello")
print(a)

b=a.copy()
print(b)

set1={1,2,3,4,5,66}
set2={11,22,333,44,55}
set3={1,2,3,5}

print(set1.isdisjoint(set2))  #It returns True when set b element not in set a
print(set3.isdisjoint(set1)) #It returns False cause set c in set a

print(set3.issubset(set1)) #check set3 is subset of set1
print(set2.issubset(set1)) #check set2 is subset of set1

print(set1.issuperset(set3)) #check set3 all element in set1
print(set1.issuperset(set2))

set1.update(set2) #Return combination of two set and return unique values
print(set1)

set3.clear() #clear the set
print(set3)

#union , intersection ,symmetric difference
print("\n\nunion , intersection ,symmetric difference\n\n")

set1={1,2,3,4,5,66}
set2={11,22,333,44,55}
set3={1,2,3,5}

print(set1.union(set3)) # combination on set1 and set2 but not repeat number
print(set1.union(set2)) # combination on set1 and set2 but not repeat number

print(set1.intersection(set3)) # return value which only in both set1 and set 3 

print(set1.symmetric_difference(set3)) #return value which are in set1 but not in set2
print(set1.symmetric_difference(set2)) 

set1.symmetric_difference_update(set3)#updates the original set by removing items that are present in both sets, and inserting the other items.
print(set1)

#use all function which are intersection_update,union_update, symmetric_differnece_update :- which can be used for update the set not to create an new updated set


#Problem Solving

#problem 1
#find min and max value from set

set1={1,2,3,4,5,66}
set2={11,22,333,4,5}
set3={1,2,3,4,5}

print(min(set2))
print(max(set2))

#Problem 2 :- return common set element

print(set(set1) & set(set2) & set(set3))

#Problem 3 :- find difference between two set

print(set1.difference(set2))

#Problem 4 :- Delete element from set

set3.discard(2)
print(set3)

#problem5 :- check set3 is subset of set1
print(set3.issubset(set1))