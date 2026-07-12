"""Módulo contendo a estrutura de dados de entrada para as simulações financeiras."""

class Cenario:
    """Representa as condições e variáveis iniciais de um cenário financeiro.

    Esta classe funciona como um container imutável de dados que encapsula 
    os parâmetros fornecidos pelo usuário para alimentar o motor de cálculo 
    do simulador.

    Attributes:
        _valor_inicial (float): O aporte inicial ou patrimônio de partida.
        _taxa_juros_mensal (float): A taxa nominal de juros ao mês (ex: 1.2 para 1.2%).
        _tempo_meses (int): O horizonte de tempo total da simulação em meses.
    """

    def __init__(self, valor_inicial: float, taxa_juros_mensal: float, tempo_meses: int):
        """Inicializa um novo cenário financeiro com os parâmetros validados.

        Args:
            valor_inicial (float): O montante inicial a ser investido (R$).
            taxa_juros_mensal (float): A taxa de juros nominal mensal em porcentagem (%).
            tempo_meses (int): O prazo total em meses que o dinheiro ficará rendendo.
        """
        self._valor_inicial = valor_inicial
        self._taxa_juros_mensal = taxa_juros_mensal
        self._tempo_meses = tempo_meses

    def getValorInicial(self) -> float:
        """Retorna o capital ou aporte inicial do cenário.

        Returns:
            float: O valor investido no mês zero.
        """
        return self._valor_inicial

    def getTaxaJurosMensal(self) -> float:
        """Retorna a taxa de juros nominal mensal definida para o cenário.

        Returns:
            float: A taxa de juros em base percentual (ex: 1.2).
        """
        return self._taxa_juros_mensal

    def getTempoMeses(self) -> int:
        """Retorna o período total de tempo estipulado para a projeção.

        Returns:
            int: A quantidade de meses da simulação.
        """
        return self._tempo_meses