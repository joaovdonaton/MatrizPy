from matriz import Matriz
import math
import random

m1 = Matriz(3, 7, val=812)
m2 = Matriz(4, 4)

m2 = Matriz.operar_com(m2, lambda x: random.randint(-5, 5))

print(str(m2))
print(str(Matriz.tamanho_na_memoria(m2)))

#print(str(m1.inserir_linha(321398, m2)))

def crazy_callback(x):
    x = math.e*x
    x = math.sqrt(x)

    return x


#print(str(Matriz.operar_com(m2, cb=crazy_callback)))
