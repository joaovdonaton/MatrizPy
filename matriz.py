"""
classe para criar matrizes de tamanho MXN
métodos:
multiplicar matrizes
adicionar matrizes
subtrair matrizes
applicar uma certa operação em todos os elementos da matriz (pode ser passando uma função lambda)
converter matriz em string
printar matriz formatada
inserir linhas
inserir colunas
set e get para elementos
achar uma sub matriz
transpor matriz
https://dev.to/fkkarakurt/matrices-and-vectors-in-game-development-67h#:~:text=A%20matrix%20can%20be%20used,Y%2C%20and%20Z%20positional%20information.
função para mostrar o uso de memória de uma matriz

"""
from random import random
from utilidade import MatrizIncompativel


class Matriz:
    def __init__(self, num_linhas, num_colunas, val=0, val_randomico=False):
        self.matriz = []
        self.num_linhas = num_linhas
        self.num_colunas = num_colunas

        for i in range(num_linhas):
            self.matriz.append([])
            for j in range(num_colunas):
                self.matriz[i].append(val if not val_randomico else random())

    def __str__(self):
        s = ''

        for i in self.matriz:
            s += ' '.join([str(j) for j in i])
            s += '\n'

        return s

    def __mul__(self, matriz2):
        if self.num_colunas != matriz2.num_linhas:
            raise MatrizIncompativel
        #nova_matriz = Matriz()
        #for i in range()

