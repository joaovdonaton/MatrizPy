from matriz import Matriz
import math
import random

m1 = Matriz(3, 7, val=8)
m2 = Matriz(4, 5, val_randomico=True)

m2 = Matriz.operar_com(m2, lambda x: random.randint(-5, 256))
print(m2)
# print(m2.remover_coluna(3).remover_linha(1).remover_coluna(3))

print(Matriz.tamanho_na_memoria(m2), 'bytes\n')

# print(str(Matriz.transpor(m2))

# print(m1.inserir_linha(0, m2))

# m3 = Matriz(1, 8, val_randomico=True)
# print(m1.inserir_coluna(7, m2).inserir_linha(2, m3))

# print(m2)
# print(Matriz.soma(m2, 2))

def crazy_callback(x):
    x = math.e * x
    x = math.sqrt(x)

    return x


# print(str(Matriz.operar_com(m2, cb=crazy_callback)))

print(Matriz.transpor(Matriz.converter_para_matriz([[1, 2, 3], [2, 1, 2], [72, 7, 7], [2, 2, 2]])))
