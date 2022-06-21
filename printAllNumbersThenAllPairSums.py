'''
Pt: Nessa função precisamos mostrar todos os valores do array e também a soma entre eles, ficando da seguinte forma:
    Exemplo: array[1, 2, 3] = 1+1, 1+2,1+3 e assim sucessivamente mostrando o resultado da soma para os numeros no array 

En: In this function we need to show all the values of the array and also the sum between them, as follows:
     Example: array[1, 2, 3] = 1+1, 1+2,1+3 and so on showing the sum result for the numbers in the array
'''

def printAllNumbersThenAllPairSums(nunbers):
    print("esse são os numeros: ")
    for i in nunbers:
        print(x)

    print('e esses sao as suas somas')
    for j in range(len(nunbers)):
        for w in range(len(nunbers)):
            first_number = nunbers[j]
            second_number = nunbers[w]
            print("passou aqui")
            teste = first_number + second_number
            print(teste)
          
array_nunbers = [1, 2, 3, 4, 5]
printAllNumbersThenAllPairSums(array_nunbers)
