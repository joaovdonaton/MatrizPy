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
https://towardsdatascience.com/the-strange-size-of-python-objects-in-memory-ce87bdfbb97f#:~:text=When%20you%20create%20a%20list,of%20references%20to%20other%20objects.
https://towardsdatascience.com/python-memory-and-objects-e7bec4a2845
https://towardsdatascience.com/how-to-define-custom-exception-classes-in-python-bfa346629bca
https://dev.to/fkkarakurt/matrices-and-vectors-in-game-development-67h#:~:text=A%20matrix%20can%20be%20used,Y%2C%20and%20Z%20positional%20information.
https://realpython.com/python3-object-oriented-programming/#define-a-class-in-python
https://www.programiz.com/python-programming/operator-overloading

"""
from random import random
from utilidade import MatrizIncompativel


class Matriz:
    def __init__(self, num_linhas, num_colunas, val=0, val_randomico=False):
        """
        Inicializar matriz de tamanho num_linhas X num_colunas com valor inicial de val, ou valores randômicos de 0-1
        se val_randomico = True
        """
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

    def set_element(self, lin, col, val):
        self.matriz[lin][col] = val

    def get_element(self, lin, col):
        return self.matriz[lin][col]

    def inserir_linha(self, pos, m_linha):
        """
        Inserir a matriz m_linha (tamanho 1xself.num_colunas) na matriz self
        """

        if m_linha.num_colunas != self.num_colunas or m_linha.num_linhas != 1 or pos > self.num_linhas:
            raise MatrizIncompativel(self, m_linha, 2, pos=pos)

        m = Matriz(self.num_linhas+1, self.num_colunas)

        s = False
        for i in range(self.num_linhas+1):
            if i == pos:
                s = True
                for j in range(self.num_colunas):
                    m.set_element(i, j, m_linha.get_element(0, j))
                continue
            for j in range(self.num_colunas):
                x, y = (i, j) if not s else (i-1, j-1)
                m.set_element(i, j, self.get_element(x, y))

        return m

    def inserir_coluna(self, pos, m_coluna):
        pass

    def __mul__(self, matriz2):
        """
        Multiplicar a matriz self pela matriz2.
        """
        if self.num_colunas != matriz2.num_linhas:
            raise MatrizIncompativel(self, matriz2, 0)

        m = Matriz(self.num_linhas, matriz2.num_colunas)
        for i in range(m.num_linhas):
            for j in range(m.num_colunas):
                soma = 0
                for k in range(self.num_colunas):
                    soma += self.get_element(i, k)*matriz2.get_element(k, i)
                m.set_element(i, j, soma)

        return m

    def __operacao_elementwise(self, matriz2, operacao):
        """
        Método base para as diferentes operações elementwise
        """

        if self.num_linhas != matriz2.num_linhas or self.num_colunas != matriz2.num_colunas:
            raise MatrizIncompativel(self, matriz2, 1)

        m = Matriz(self.num_linhas, self.num_colunas)
        for i in range(self.num_linhas):
            for j in range(self.num_colunas):
                m.set_element(i, j, eval(str(self.get_element(i, j)) + operacao + str(matriz2.get_element(i, j))))

        return m

    def __add__(self, matriz2):
        """
        Adicionar a matriz self à matriz2
        """

        return self.__operacao_elementwise(matriz2, '+')

    def __sub__(self, matriz2):
        """
        Subtrair a matriz self pela matriz2
        """

        return self.__operacao_elementwise(matriz2, '-')

    @staticmethod
    def operar_com(m, cb):
        """
        Aplica a operação do parâmetro cb (função callback) em todos os elementos da matriz m
        """

        m_novo = Matriz(m.num_linhas, m.num_colunas)
        for i in range(m.num_linhas):
            for j in range(m.num_colunas):
                m_novo.set_element(i, j, cb(m.get_element(i, j)))

        return m_novo

    @staticmethod
    def tamanho_na_memoria():
        """
        Método para calcular o tamanho na memória da nossa matriz (que é a lista contida no membro self.matriz)
        """



