'''
Pt br: Nesse challenge eu precisei criar uma função juntando os pares de um array. Nesse exemplo não estamos falando de numeros pares - como na matematica - mas numero vizinho ao outro
   Exemplo: array[1, 2, 3] ficará 1 1, 1 2, 1 3, 2 1, 2 2, 2 3, 3 1, 3 2, 3 3
   
Eng: In this challenge I need to create a function by joining the pairs of an array. In this example we are not talking about even numbers - as in mathematics - but numbers next to each other
   Example: array[1, 2, 3] 1 1, 12, 1 3, 2 1, 2 2, 2 3, 3 1, 3 2, 3 3
'''

# A function knowing the range of my array
def logAllPairOfArray(array):
 for i in range(5):
    for j in range(5):
      new_array = array[i]
      new_array2 = array[j]
      print(new_array, new_array2)

# A function not knowing the range of my array
def lotAllPairOfArray2(array):
  for i in range(len(array)):
    for j in range(len(array)):
      new_array_i = array[i]
      new_array_j = array[j]
      print(new_array_i, new_array_j)
 
boxes = [1, 2, 3, 4, 5]
lotAllPairOfArray2(boxes)