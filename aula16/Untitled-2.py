# Criando uma matriz tridimensional de tamanho 3x3x3 com valores específicos
matriz_tridimensional = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                        [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                        [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]

# Percorrendo e imprimindo os elementos da matriz
print("Elementos da matriz tridimensional:")
for i in range(3):
    for j in range(3):
        for k in range(3):
            print(matriz_tridimensional[i][j][k], end=" ")
        print()  # Adiciona uma quebra de linha após imprimir todos os elementos de uma linha
    print()  # Adiciona uma linha em branco entre as "camadas" da matriz
