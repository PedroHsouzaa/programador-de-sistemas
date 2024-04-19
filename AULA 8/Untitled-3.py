print("1-converter celsius para fahrenheit")
print("2-converter fahrenheit para celsius")
escolha = int(input("conversao escolhida?: "))

match escolha:
    case 1:
        celsius= float(input("escolha sua temperatura em celsius: "))
        print("a temperatura em fahrenheit",(celsius*9/5)+32)
    case 2: 
        fahrenheit = float(input("escolha sua temperatura em fahrenheit: "))
        print("a temperatura em celsius e :",(fahrenheit-32)*5/9)
    case _:
        print("invalido")

#lembrar de sempre começar declarando as variaveis e oq pedir para o usuario
