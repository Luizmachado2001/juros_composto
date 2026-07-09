class Resultado:
    """
    Representa o relatório de saída de uma simulação financeira.

    Esta classe armazena os valores calculados finais e gerencia a lógica de 
    formatação e exibição visual do resumo do investimento para o usuário.
    """

    def __init__(self, montante_final, total_juros_ganhos):
        """
        Inicializa o objeto de resultado com os valores calculados.

        Args:
            montante_final (float): O valor total acumulado ao fim do período.
            total_juros_ganhos (float): O valor total de juros gerados na simulação.
        """
        self.montante_final = montante_final
        self.total_juros_ganhos = total_juros_ganhos

    def exibirResumo(self):
        """
        Gera e exibe um relatório formatado no terminal com os dados do investimento.

        Formata os valores internamente para o padrão de moeda brasileiro (PT-BR)
        com separadores de milhares por ponto e decimais por vírgula.
        """
        # Formatando os valores para o padrão BR antes de exibir
        montante_br = f"{self.montante_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        juros_br = f"{self.total_juros_ganhos:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        
        print(35 * "=")
        print("       RESUMO DO INVESTIMENTO     ")
        print(35 * "=")
        print(f"Montante Final:        R$ {montante_br}")
        print(f"Total de Juros Ganhos: R$ {juros_br}")
        print(35 * "=")