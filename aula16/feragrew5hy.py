# Criando uma matriz tridimensional de tamanho 2x2x2 com valores específicos
matriz_tridimensional = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

# Percorrendo e imprimindo os elementos da matriz
print("Elementos da matriz tridimensional:")
for i in range(2):
    for j in range(2):
        for k in range(2):
            print(matriz_tridimensional[i][j][k], end=" ")
            if k == 1: #verifica se estamos na última coluna da linha e, se sim, adiciona uma quebra de linha após imprimir todos os elementos da linha.
                print()  # Adiciona uma quebra de linha após imprimir todos os elementos de uma linha
    print()  # Adiciona uma linha em branco entre as "camadas" da matriz
