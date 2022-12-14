class MatrizIncompativel(Exception):
    def __init__(self, m1, m2, msg, pos=None):
        """
        O parâmetro msg é o código da mensagem de erro
        """
        self.m1 = f"{m1.num_linhas}x{m1.num_colunas}"
        self.m2 = f"{m2.num_linhas}x{m2.num_colunas}"
        self.pos = pos
        self.msg = msg

    def __str__(self):
        if self.msg == 0:  # multiplicação inválida
            return f"""Não é possível multiplicar uma matriz de tamanho {self.m1} por 
                   uma de tamanho {self.m2}"""
        elif self.msg == 1:  # operação inválida
            return f"""Não é possível fazer esta operação com duas matrizes de tamanhos diferentes 
            {self.m1} por {self.m2}"""
        elif self.msg == 2:  # impossível inserir linha/coluna
            return f"""Não é possível inserir esta linha/coluna ({self.m2}) na posição {self.pos} matriz de tamanho {self.m1}.
            A quantidade de colunas/linhas da linha/coluna deve ser igual à da matriz.
            Pos não pode ser maior que o tamanho de linhas/colunas da matriz"""


class EixoInvalido(Exception):
    def __init__(self, eixo):
        self.eixo = eixo

    def __str__(self):
        return f"O eixo {self.eixo} não representa um eixo válido."


class PosicaoInvalida(Exception):
    def __init__(self, pos, pos_max, m):
        self.pos = pos
        self.pos_max = pos_max
        self.m = f"{m.num_linhas}x{m.num_colunas}"

    def __str__(self):
        return f"O índice de posição ({self.pos}) deve ser menor que ou igual a {self.pos_max} na matriz de tamanho {self.m}"


class ListaInvalida(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        if self.msg == 0:
            return 'Falha na conversão da lista para Matriz. Alguma das linhas não é uma lista.'
        elif self.msg == 1:
            return 'Falha na conversão da lista para Matriz. O Número de colunas deve ser igual em todas as linhas.'

