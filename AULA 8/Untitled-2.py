turno = input("informe seu turno de trabalho. ")

match turno:
    case "m":
        print("bom dia ")
    case "v":
        print("boa tarde")
    case "n":
        print("boa noite")
    case _:
        print("invalido")