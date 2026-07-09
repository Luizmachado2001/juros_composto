class Cenario:
    def __init__(self, valor_inicial, taxa_juros_mensal, tempo_meses):
        """
        Representa o cenário de entrada para uma simulação financeira.
        Esta classe encapsula os dados fundamentais necessários para os cálculos
        de juros compostos, como o capital inicial, a taxa de rendimento e o período.
        """
        self.valor_inicial = valor_inicial
        self.taxa_juros_mensal = taxa_juros_mensal
        self.tempo_meses = tempo_meses

    def getValorInicial(self) -> float:
        """
        Retorna o capital/valor inicial investido no início do cenário.

        Returns:
            float: O montante inicial.
        """
        return self.valor_inicial
    
    def getTaxaJurosMensal(self) -> float:
        """
        Retorna a taxa de juros cobrada ou rendida mensalmente (em porcentagem).

        Returns:
            float: A taxa de juros mensal (ex: 1.0 para 1%).
        """
        return self.taxa_juros_mensal
    
    def getTempoMeses(self) -> int:
        """
        Retorna o período total de tempo estipulado para o cenário, em meses.

        Returns:
            int: A quantidade de meses.
        """
        return self.tempo_meses