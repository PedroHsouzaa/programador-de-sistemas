nota_1 = int(input("Dgite sua prieira nota: "))
nota_2 = int(input("Digite sua segunda nota: "))
nota_3 = int(input("Digite sua terceira nota: "))
nota_4 = int(input("Digite sua quarta nota: "))
media = (nota_1+nota_2+nota_3+nota_4)/4
if media >= 7:
    print("Aprovado!!!",media)
else:
    print("Reprovado",media)