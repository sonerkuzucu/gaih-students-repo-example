#Explain your work

#Question 1
List1 = list(range(2, 11, 2))
print (List1)
List2 = list(range(1, 10, 2))
print (List2)
List = List1 + List2
print (List)
List.sort()
print (List)

Listx2 = [a*2 for a in List]
print (Listx2)

for x in range(len(Listx2)):
  print (List[x], type(Listx2[x]))
