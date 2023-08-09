#Escreva uma função que imprime todos os números primos entre 1 e 50 
#Dica: um número é primo se ele for divisível apenas por 1 e ele mesmo, 
#use o operador % (resto da divisão) para isso.
print("Lista com os numeros")
def verificacao_primos():
    lista_numeroprimo1 = []
    contador = 0 

    for i in range(1, 51):
        if i%1 == 0 and i%i == 0:
            contador += 2
        if i%2 == 0:
            contador += 1
        if contador == 2:
            lista_numeroprimo1.append(i)
        contador = 0

    return lista_numeroprimo1

print(verificacao_primos())
