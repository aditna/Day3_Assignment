num = 1000
 
if num > 1:
  for j in range(2,num):
    for i in range(2, j):
      if (j % i) == 0:
        print(j, "is not a prime number")
        break      
      else:
        print(j, "is a prime number")
        break
 
else:
    print(j, "is not a prime number")