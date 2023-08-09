#Faça uma função que determina se um número é par ou ímpar. 
#Use o % para determinar o resto de uma divisão.Por exemplo: 3 % 2 = 1 e 4 % 2 = 0

def contador():
    a = int(input("Digite um número: "))
    if a%2 == 0:
        print("O número é par")
    else:
        print("O número é impar")

contador()