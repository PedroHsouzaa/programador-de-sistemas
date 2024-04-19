acumulador = 0
num = int(input("informe um numero: "))

while num != 0:
    acumulador += num
    num = int(input("informe um numero"))
    
print(acumulador)