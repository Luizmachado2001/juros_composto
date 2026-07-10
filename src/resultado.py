import matplotlib.pyplot as plt

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
        Gera e exibe um relatório formatado no terminal com os dados do investimento
        e um gráfico de barras comparativo.
        """
        # Formatando os valores para o padrão BR antes de exibir no terminal
        montante_br = f"{self.montante_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        juros_br = f"{self.total_juros_ganhos:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        
        print(35 * "=")
        print("       RESUMO DO INVESTIMENTO     ")
        print(35 * "=")
        print(f"Montante Final:        R$ {montante_br}")
        print(f"Total de Juros Ganhos: R$ {juros_br}")
        print(35 * "=")

        #self.mostrarGrafico()

    def mostrarGrafico(self):
        """
        Gera, configura e exibe um gráfico de barras comparativo dos resultados.

        Este método utiliza a biblioteca matplotlib para criar um gráfico de barras
        com o objetivo de contrastar visualmente o montante final acumulado e o 
        total de juros ganhos. Cada barra é personalizada com uma cor distinta 
        para facilitar a diferenciação visual.

        Attributes:
            categorias (list de str): Rótulos do eixo X ('Montante Final', 'Juros Ganhos').
            valores (list de float): Os valores financeiros correspondentes a cada categoria.

        Note:
            Este método depende da biblioteca 'matplotlib.pyplot' importada como 'plt'
            e assume que o ambiente de execução possui suporte para exibição de 
            interfaces gráficas (GUI) ao invocar o método `plt.show()`.
        """

        # ---- Correção do Gráfico (Barras) ----
        categorias = ['Montante Final', 'Juros Ganhos']
        valores = [self.montante_final, self.total_juros_ganhos]

        # Cria as barras com cores diferentes
        plt.bar(categorias, valores, color=['#4CAF50', '#FF9800'])
        
        plt.title("Comparativo do Rendimento (R$)")
        plt.ylabel("Valores")
        
        # Mostra o gráfico na tela
        plt.show()