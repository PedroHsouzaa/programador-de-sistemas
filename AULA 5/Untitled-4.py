num_1 = float(input("Digite sua primeira nota: "))
num_2 = float(input("Digite sua segunda nota: "))
num_3 = float(input("Digite sua terceira nota: "))
num_4 = float(input("Digite sua quarta nota: "))
media = (num_1+num_2+num_3+num_4)/4
if media >= 7:
    print("aprovado")
else: 
    if media >= 5:
        print("recuperaçao")
    else:
        print("reprovado")    
