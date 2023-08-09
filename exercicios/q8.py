#Agora «vá à sorveteria» e se empanturre e sorvete e tire o sorvete da lista.

lista_compras = []
def add_itens(nome, categoria):
    lista_compras.append({"nome": nome, "categoria": categoria})

add_itens("Sabão em pó", "Limpeza")
add_itens("Sabão em barra", "Limpeza")
add_itens("Água sanitária", "Limpeza")
add_itens("Sorvete", "Sobremesas")


for itens in lista_compras:
    print(f"Item: {itens['nome']} \nCategoria: {itens['categoria']}\n")



def remover_itensporcateg(categoria):
    global lista_compras
    lista_compras = [itens for itens in lista_compras if itens['categoria'] != categoria]
    

remover_itensporcateg("Limpeza")
for itens in lista_compras:
    print("--pós remoção--")
    print(f"Item: {itens['nome']} \nCategoria: {itens['categoria']}\n")

remover_itensporcateg("Sobremesas")
if len(lista_compras) == 0:
    print("A lista agora está vazia")