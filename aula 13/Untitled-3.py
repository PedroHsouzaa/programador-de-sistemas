eleitores = int(input(" Qual a quantidade de eleitores: "))
print("Tiao do gas-2101, shaolin matador de porco-2403, ze da manga-1202")
tiao = 0
shaolin = 0 
ze = 0 
for i in range(eleitores):
    voto = int(input("digite seu voto"))
    if voto == 2101:
        tiao += 1
    if voto == 2403:
        shaolin += 1
    if voto == 1202:
        ze += 1
print("a quantidade de votos do tiao e igual a",tiao)
print("a quantidade de votos do tiao e igual a",shaolin)
print("a quantidade de votos do tiao e igual a",ze)
        