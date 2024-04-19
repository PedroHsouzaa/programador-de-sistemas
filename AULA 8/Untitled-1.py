dia = int(input("informe o dia: "))

match dia:
    case 1:
        print("domingo")
    case 2:
        print("segunda")
    case 3:
        print("terça")
    case 4:
        print("qurta")
    case 5:
        print("quinta")
    case 6:
        print("sexta")
    case 7:
        print("sabado")
    case _:
        print("invalido")
