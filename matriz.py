"""
classe para criar matrizes de tamanho MXN
métodos:
multiplicar matrizes - FEITO
adicionar matrizes - FEITO
subtrair matrizes - FEITO
applicar uma certa operação em todos os elementos da matriz (pode ser passando uma função lambda) - FEITO
converter matriz em string - FEITO
printar matriz formatada - FEITO
inserir linhas - FEITO
inserir colunas - FEITO
set e get para elementos - FEITO
achar uma sub matriz -
transpor matriz - FEITO
https://dev.to/fkkarakurt/matrices-and-vectors-in-game-development-67h#:~:text=A%20matrix%20can%20be%20used,Y%2C%20and%20Z%20positional%20information.
função para mostrar o uso de memória de uma matriz - FEITO

"""
from random import random
from utilidade import MatrizIncompativel, EixoInvalido
from sys import getsizeof


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

    def set_element(self, linha, coluna, val):
        self.matriz[linha][coluna] = val

    def get_element(self, linha, coluna):
        return self.matriz[linha][coluna]

    def inserir_linha(self, pos, m_linha):
        """
        Inserir a matriz m_linha (tamanho 1xself.num_colunas) na matriz self
        """

        if m_linha.num_colunas != self.num_colunas or m_linha.num_linhas != 1 or pos > self.num_linhas:
            raise MatrizIncompativel(self, m_linha, 2, pos=pos)

        m = Matriz(self.num_linhas + 1, self.num_colunas)
        m.matriz = self.matriz.copy()
        m.matriz.insert(pos, m_linha.matriz[0])

        return m

    def inserir_coluna(self, pos, m_coluna):
        """
        Inserir a matriz m_coluna (tamanho self.num_linhasx1) na matriz self
        """

        if m_coluna.num_linhas != self.num_linhas or m_coluna.num_colunas != 1 or pos > self.num_colunas:
            raise MatrizIncompativel(self, m_coluna, 2, pos=pos)

        m = Matriz(self.num_linhas, self.num_colunas+1)
        m.matriz = self.matriz.copy()

        for i in range(m.num_linhas):
            m.matriz[i].insert(pos, m_coluna.get_element(i, 0))

        return m

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
                    soma += self.get_element(i, k) * matriz2.get_element(k, j)
                m.set_element(i, j, soma)

        return m

    def operacao_elementwise(self, matriz2, operacao):
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

        return self.operacao_elementwise(matriz2, '+')

    def __sub__(self, matriz2):
        """
        Subtrair a matriz self pela matriz2
        """

        return self.operacao_elementwise(matriz2, '-')

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
    def tamanho_na_memoria(m):
        """
        Método para calcular o tamanho na memória da nossa matriz (que é a lista contida no membro self.matriz)
        O object de uma lista vazia no python usa 56bytes, para cada elemento que adicionamos isso aumenta em 8bytes.
        As listas armazenam referências aos seus itens e não os itens em sí.
        Otimização de memoria do python (interning) para integers entre [-5,256] pode atrapalhar o nosso cálculo, por
        isso temos que ter uma list "ids" para rastrear quais endereços de memórias se encaixam no interning e não
        contá-los mais de uma vez
        """

        ids = []
        tam_total = getsizeof([])
        for i in range(m.num_linhas):
            tam_total += 8
            for j in range(m.num_colunas):
                if id(m.matriz[i][j]) in ids:
                    continue
                tam_total += 8
                ids.append(id(m.matriz[i][j]))

        return tam_total

    @staticmethod
    def transpor(m):
        """
        Transpor a matriz m
        """

        m_novo = Matriz(m.num_colunas, m.num_linhas)

        for i in range(m.num_linhas):
            for j in range(m.num_colunas):
                m_novo.set_element(j, i, m.get_element(i, j))

        return m_novo

    @staticmethod
    def soma(m, eixo):
        """
        Fazer uma soma dos elementos da matrix ao longo de um certo eixo
        eixo = 0 (soma as linhas, retorna uma coluna), eixo = 1 (soma as colunas, retorna uma linha),
        eixo = 2 soma tudo (retorna matriz 1x1)
        """

        if eixo not in [0, 1, 2]:
            raise EixoInvalido(eixo)

        if eixo == 0:
            m_novo = Matriz(m.num_linhas, 1)
            for i in range(m.num_linhas):
                m_novo.set_element(i, 0, sum(m.matriz[i]))

            return m_novo

        elif eixo == 1:
            m_novo = Matriz(1, m.num_colunas)
            for i in range(m.num_colunas):
                s = 0
                for j in range(m.num_linhas):
                    s += m.get_element(j, i)

                m_novo.set_element(0, i, s)

            return m_novo

        elif eixo == 2:
            m_novo = Matriz(1, 1)
            s = 0
            for i in range(m.num_linhas):
                s += sum(m.matriz[i])

            m_novo.set_element(0, 0, s)

            return m_novo
