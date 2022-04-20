def perfectN(n):
  total = 0
  
  list1 = list(range(1,n))
  for i in list1:
    
    if (n % i == 0):
      total += i
  
  return (n == total)    

list2 = list(range(1,1001))

for n in list2:
  
  if (perfectN(n)):
    print(n, "is perfect number")
    
    
# Version 2:

"""

def perfectN(n):
  total = 0
  
  list1 = list(range(1,n))
  for i in list1:
    
    if (n % i == 0):
      total += i
  
  if (n == total):
    print("Mükemmel Sayı: ", n)      

list2 = list(range(1,1001))

for n in list2:
  
  if (perfectN(n)):
    print()

"""

    

    
  