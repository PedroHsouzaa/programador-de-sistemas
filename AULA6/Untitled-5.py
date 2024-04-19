valor = float(input("coloque o valor da compra: "))
pagamento = (input("coloque a forma de pagamento: "))
if pagamento == "d":
    print(valor,*0.95)
elif pagamento == "c":
    print(valor)
else:
    print("invalido")