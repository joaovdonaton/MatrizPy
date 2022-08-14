from matriz import Matriz
import math

print("Podemos criar uma matriz 7x7 com valor inicial 3 =>", 'm = Matriz(7, 7, val=3)')
m = Matriz(7, 7, val=3)
print(m)
input("Continuar...")

print("Matriz 7x3 com valor inicial de 9 =>", 'm3 = Matriz(7, 3, 9)')
m3 = Matriz(7, 3, 9)
print(m3)
input("Continuar...")

print("Podemos também criar uma matriz 1x7 com valores iniciais aleatório entre 0-1 => m2 = Matriz(1, 7, "
      "val_randomico=True)")
m2 = Matriz(1, 7, val_randomico=True)
print(m2)
input("Continuar...")

print("Podemos acessar e alterar elementos individualmente => set_element(1, 2, 55) e get_element(1, 2)")
m.set_element(1, 2, 55)
print(m.get_element(1, 2))
print(m)
input("Continuar...")

print("Também é possível inserir linhas e colunas => m.inserir_linha(4, m2)")
print(m.inserir_linha(4, m2))
input("Continuar...")

print(f"""O uso de operadores como *, - e + entre matrizes
m*m3
{m*m3}
m+m
{m+m}
m-m
{m-m}""")
input("Continuar...")

print(f"""Também é possível utilizar o método operacao_elementwise para realizar operacacoes elementwise
=> m.operacao_elementwise(m, '*')
{m.operacao_elementwise(m, '*')}""")
input("Continuar...")

print(f"""podemos usar o método operar_com para passar um callback que será aplicado a todos os elementos da matriz
=> Matriz.operar_com(m, lambda x: math.sqrt(x))
{Matriz.operar_com(m, lambda x: math.sqrt(x))}""")
input("Continuar...")

print(f"""método para calcular o tamanho da lista que representa a matriz na memória.
=> Matriz.tamanho_na_memoria(m)
{Matriz.tamanho_na_memoria(m)} bytes""")
input("Continuar...")

print(f"""com o método soma, também é possível somar ao longo de um certo eixo da matriz, ou somar todos os elementos
=> Matriz.soma(m3, 0)
{Matriz.soma(m3, 0)}
=> Matriz.soma(m3, 1)
{Matriz.soma(m3, 1)}
=> Matriz.soma(m3, 2)
{Matriz.soma(m3, 2)}""")
input("Continuar...")

print(f"""O método converter_para_matriz converte uma lista 2D para um objeto Matriz
=> converter_para_matriz([[1, 2, 3], [2, 1, 2], [72, 7, 7], [2, 2, 2]])
{Matriz.converter_para_matriz([[1, 2, 3], [2, 1, 2], [72, 7, 7], [2, 2, 2]])}""")
input("Continuar...")

print("O método transpor transpõe a matriz m => Matriz.transpor(m3)")
print(Matriz.transpor(m3))
