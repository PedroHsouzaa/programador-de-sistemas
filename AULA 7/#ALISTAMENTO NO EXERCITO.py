
sexo = input("Digite seu sexo: ")
altura = float(input("Digite sua altura: "))

if sexo == "m":
    if altura >= 1.70:
        print("aprovado")
    else:
        print("reprovado")
        
elif sexo == "f":
    if altura>= 1.60:
        print("aprovado")
    else:
        print("invalido")




