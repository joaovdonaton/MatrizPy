from matriz import Matriz
import math

m1 = Matriz(3, 3, val_randomico=True)
m2 = Matriz(3, 3, 2)

print(str(m1))
print(str(m2))

#print(str(m1+m2))


def crazy_callback(x):
    x = math.e*x
    x = math.sqrt(x)

    return x


print(str(Matriz.operar_com(m2, cb=crazy_callback)))
