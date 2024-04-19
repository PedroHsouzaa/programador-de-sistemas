conversao = input("converter c/f ou f/c?: ")
temperatura = float(input("digite sua temperatura: "))
if conversao == "c/f":
    print("c/f",(temperatura*9/5)+32)
elif conversao == "f/c":
    print("f/c",(temperatura-32)*5/9)
else:
    print ("invalido")
    
