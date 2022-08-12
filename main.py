from matriz import Matriz
import math

m1 = Matriz(3, 7, val=812)
m2 = Matriz(1, 7, 2)

print(str(m1))
print(str(m2))

print(str(m1.inserir_linha(321398, m2)))

def crazy_callback(x):
    x = math.e*x
    x = math.sqrt(x)

    return x


#print(str(Matriz.operar_com(m2, cb=crazy_callback)))
