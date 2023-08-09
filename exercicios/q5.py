#Utilizando o del, remova todos os elementos da lista criada anteriormente até a lista ficar vazia.
import random

idades = [random.randint(1, 80) for a in range(20)]
print(idades)

print(len(list(idades)))

del idades