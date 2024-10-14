vetor = []
for i in range(10) :
    numeros = int(input("Insira os numeros:"))
    vetor.append(numeros)
for numeros in vetor:
    if numeros%2 != 0:
        print(numeros)