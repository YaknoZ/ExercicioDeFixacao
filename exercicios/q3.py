#Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média. 
notas = []
for i in range(4):
    notas.append(float(input("Digite as 4 notas em ordem: ")))
print("-------Notas-------")
for i in range(4):
    print("Av ", i+1, ":", float(notas[i]))

print("Média final: ", (notas[0]+ notas[1] + notas[2] + notas[3])/4)
