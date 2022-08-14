from matriz import Matriz
import math

print("Podemos criar uma matriz 7x7 com valor inicial 3 =>", 'm = Matriz(7, 7, val=3)')
m = Matriz(7, 7, val=3)
print(m)

print("Matriz 7x3 com valor inicial de 9 =>", 'm3 = Matriz(7, 3, 9)')
m3 = Matriz(7, 3, 9)
print(m3)

print("Podemos também criar uma matriz 1x7 com valores iniciais aleatório entre 0-1 => m2 = Matriz(1, 7, val_randomico=True)")
m2 = Matriz(1, 7, val_randomico=True)
print(m2)

print("Podemos acessar e alterar elementos individualmente => set_element(1, 2, 55) e get_element(1, 2)")
m.set_element(1, 2, 55)
print(m.get_element(1, 2))
print(m)

print("Também é possível inserir linhas e colunas => m.inserir_linha(4, m2)")
print(m.inserir_linha(4, m2))

print("O uso de operadores como *, - e + entre matrizes")
print("m*m3")
print(m*m3)
print('m+m')
print(m+m)
print('m-m')
print(m-m)

print("Também é possível utilizar o método operacao_elementwise para realizar operacacoes elementwise")
print("=> m.operacao_elementwise(m, '*')")
print(m.operacao_elementwise(m, '*'))

print('podemos usar o método operar_com para passar um callback que será aplicado a todos os elementos da matriz')
print('=> Matriz.operar_com(m, lambda x: math.sqrt(x))')
print(Matriz.operar_com(m, lambda x: math.sqrt(x)))

print('método para calcular o tamanho da lista que representa a matriz na memória.')
print('Matriz.tamanho_na_memoria(m)')
print(Matriz.tamanho_na_memoria(m), 'bytes')

print("com o método soma, também é possível somar ao longo de um certo eixo da matriz, ou somar todos os elementos")
print(Matriz.soma(m3, 0))  # soma ao longo das linhas
print(Matriz.soma(m3, 1))  # soma ao longo das colunas
print(Matriz.soma(m3, 2))  # soma todos os elementos
