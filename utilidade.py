import matriz


class MatrizIncompativel(Exception):
    def __init__(self, m1, m2, msg):
        """
        O parâmetro msg é o código da mensagem de erro
        """
        self.m1 = m1
        self.m2 = m2
        self.msg = msg

    def __str__(self):
        if self.msg == 0:  # multiplicação inválida
            return f"""Não é possível multiplicar uma matriz de tamanho {self.m1.num_linhas}x{self.m1.num_colunas} por 
                   f"uma de tamanho {self.m2.num_linhas}x{self.m2.num_colunas}"""
        elif self.msg == 1:  # adição inválida
            return f"""Não é possível adicionar duas matrizes de tamanhos diferentes 
            {self.m1.num_linhas}x{self.m1.num_colunas} por {self.m2.num_linhas}x{self.m2.num_colunas}"""
