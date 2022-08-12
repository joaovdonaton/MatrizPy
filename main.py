from matriz import Matriz
import math
import random

m1 = Matriz(3, 7, val=812)
m2 = Matriz(3, 1, val_randomico=True)

m2 = Matriz.operar_com(m2, lambda x: random.randint(-5, 5))

print(m2)
print(Matriz.tamanho_na_memoria(m2), 'bytes\n')
#print(str(Matriz.transpor(m2))

# print(m1.inserir_linha(0, m2))

m3 = Matriz(1, 8, val_randomico=True)
print(m1.inserir_coluna(7, m2).inserir_linha(2, m3))

def crazy_callback(x):
    x = math.e*x
    x = math.sqrt(x)

    return x


#print(str(Matriz.operar_com(m2, cb=crazy_callback)))
