ef SimpleAdding(num): 
  
  answer = 0

  # loop from 1 to num
  for i in range(1, num+1):
    answer = answer + i
    
  return answer
    
print SimpleAdding(4)  
