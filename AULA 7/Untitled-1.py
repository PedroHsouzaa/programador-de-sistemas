lado_1 = float(input("escreva o lado do triangulo: "))
lado_2 = float(input("escreva o lado do triangulo: "))
lado_3 = float(input("escreva o lado do triangulo: "))
if lado_1==lado_2==lado_3:
    print("equilatero")
elif lado_1== lado_2 != lado_3 or lado_1 == lado_3 != lado_2 or lado_2 == lado_3 != lado_1 or lado_1 != lado_2 == lado_3:
    print("isoscelis")
else:
   print("escaleno")


   

