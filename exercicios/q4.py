#Ler um vetor com 20 idades e exibir a maior e menor.
import random

idades = [random.randint(1, 80) for i in range(20)]
print(idades)

idades.sort()
print("numeros ordenados", idades)