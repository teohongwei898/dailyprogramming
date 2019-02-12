givenlist = [7, 5, 4, 4, 2, 1, -3, -4, -6]

total = 0
j = len(givenlist)-1
while givenlist[j]<0:
  total += givenlist[j]
  j -= 1
print (total)
  
