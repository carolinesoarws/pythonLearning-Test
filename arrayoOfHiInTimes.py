# testing and understanding the Space Complexity 
def arrayoOfHiInTimes(n):
  hiArray = []
  i = 0
  while i < n:
    hiArray.insert(i,'hi')
    i += 1
  return hiArray
  
returnarray = arrayoOfHiInTimes(6)
print(returnarray)
