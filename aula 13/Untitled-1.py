numero = int(input("Digite um número inteiro entre 1 e 10 para gerar sua tabuada: "))

for i in range(1,11,1):
    print(numero,"x",i,"=",numero*i)
else:
    print("tabuada somente ate o 10")