List1 = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 7, 8, 8]
List2 = []

for i in List1 :  
   if i not in List2 :  
      List2.append(i)
   else :
      continue
print(List2)
      
      
