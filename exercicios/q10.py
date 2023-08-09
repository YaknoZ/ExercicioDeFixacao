#Duas palavras são um “par inverso” 
#se uma for o contrário da outra. Escreva uma função que dado duas palavras,retorne True caso sejam.

def sao_inversos(palavra1, palavra2):
    return palavra1 == palavra2[::-1]

print("Palavra 1 : Pindamonhangaba \nPalavra2 : abagnahnomadniP")
print(sao_inversos(palavra1="Pindamonhangaba", palavra2="abagnahnomadniP"))

print("Palavra 1: Celular bom \nPalavra 2: Iphone")
print(sao_inversos(palavra1="Celular", palavra2="Iphone"))