#Ler uma lista de 10 números reais e mostre-os na ordem inversa. 
lista = listaNumeros = [15, 39, 89, 76, 44, 32, 6, 99, 32, 10]
for i in range(len(lista) -1, -1, -1):
    print("Posição ", i, ":", int(lista[i]))