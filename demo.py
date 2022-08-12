from matriz import Matriz
import math

m = Matriz(7, 7, val=3)  # criar uma matriz 7x7 com valor inicial de 3
m2 = Matriz(1, 7, val_randomico=True)  # criar uma matriz 1x7 com valores inicias randômicos de 1x7

print(m)  # podemos converter a nossa matriz em uma string e printar

# podemos alterar e acessar os elementos da matriz individualmente
m.set_element(1, 2, 55)
print(m.get_element(1, 2))

# podemos inserir linhas/colunas na matriz
print(m.inserir_linha(4, m2))

# também é possível usar operadores como *, +, - entre matrizes
m3 = Matriz(7, 3, 9)
print(m*m3)  # multiplicação de matrizes
print(m+m)  # adição
print(m-m)  # subtração
print(m.operacao_elementwise(m, '*'))  # também podemos realizar operações element wise

# podemos usar o método operar_com para passar um callback que será aplicado a todos os elementos da matriz
print(Matriz.operar_com(m, lambda x: math.sqrt(x)))

# método para calcular o tamanho da lista que representa a matriz na memória.
print(Matriz.tamanho_na_memoria(m), 'bytes')
