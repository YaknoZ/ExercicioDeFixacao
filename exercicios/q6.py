#Faça uma lista de compras do mês, não se esqueça de comprar produtos de limpeza e sorvete!
lista_compras = []

def add_itens(nome, categoria):
    lista_compras.append({"nome": nome, "categoria": categoria})

add_itens("Sabão em pó", "Limpeza")
add_itens("Sabão em barra", "Limpeza")
add_itens("Água sanitária", "Limpeza")
add_itens("Sorvete", "Sobremesas")


for itens in lista_compras:
    print(f"Item: {itens['nome']} \nCategoria: {itens['categoria']}\n")
