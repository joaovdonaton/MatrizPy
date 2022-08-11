import matriz

class MatrizIncompativel(Exception):
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __str__(self):
        return f"Não é possível multiplicar uma matriz de tamanho {self.m1.num_linhas}x{self.m1.num_colunas} por uma " \
               f"de tamanho {self.m2.num_linhas}x{self.m2.num_colunas}"
