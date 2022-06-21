'''
Pt br: Nesse challenge eu precisei criar uma função juntando os pares de um array. Nesse exemplo não estamos falando de numeros pares - como na matematica - mas numero vizinho ao outro
   Exemplo: array[1, 2, 3] ficará 1 1, 1 2, 1 3, 2 1, 2 2, 2 3, 3 1, 3 2, 3 3
   
   Esse código tem a responsabilidade de entender como funcionaria o codigo utilizandoa as regras do Big O, ou seja tentando fazer 
   um código mais performatico 
   
  Eng: In this challenge I need to create a function by joining the pairs of an array. In this example we are not talking about even numbers - as in mathematics - but numbers next to each other
   Example: array[1, 2, 3] 1 1, 12, 1 3, 2 1, 2 2, 2 3, 3 1, 3 2, 3 3

   This code has the responsibility of understanding how the code would work using the Big O rules, that is, trying to make
    a more performative code

'''

def lotAllPairOfArray2(array):
  for i in range(len(array)):
    new_array_i = array[i]


  for j in range(len(array)):
    new_array_j = array[j]

  print(new_array_i, new_array_j)
 
boxes = [1, 2, 3, 4, 5]
lotAllPairOfArray2(boxes)