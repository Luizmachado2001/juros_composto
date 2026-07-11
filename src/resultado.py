import matplotlib.pyplot as plt
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Inicializa o console global do Rich
console = Console()

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

    def exibirResumo(self, mostrar_grafico=True):
        """
        Gera e exibe um relatório formatado e elegante no terminal usando a biblioteca Rich.

        Args:
            mostrar_grafico (bool, opcional): Define se o gráfico de barras comparativo
                deve ser exibido na tela após o resumo textual. O padrão é True.
        """
        # Formatando os valores para o padrão BR
        montante_br = f"R$ {self.montante_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        juros_br = f"R$ {self.total_juros_ganhos:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        
        # Construindo o texto estilizado
        texto_resumo = Text()
        texto_resumo.append("Montante Final:        ", style="bold white")
        texto_resumo.append(f"{montante_br}\n", style="bold green")
        texto_resumo.append("Total de Juros Ganhos: ", style="bold white")
        texto_resumo.append(f"{juros_br}", style="bold yellow")

        # Criando o painel moderno combinando com o resto do sistema
        painel = Panel(
            texto_resumo, 
            title="[bold blue]RESUMO DO INVESTIMENTO[/bold blue]", 
            expand=False, 
            border_style="blue"
        )
        
        console.print("\n")
        console.print(painel)
        console.print("\n")

        # Mantendo o controle dinâmico (ou seu modo mecânico via comentário)
        if mostrar_grafico:
            self.mostrarGrafico()

    def mostrarGrafico(self):
        """
        Gera, configura e exibe um gráfico de linha e área moderno e otimizado.

        Este método utiliza a biblioteca matplotlib para criar uma curva de crescimento,
        aplicando um estilo moderno (grid sutil, preenchimento gradiente e marcadores)
        que facilita a visualização do efeito exponencial do investimento.
        """
        import matplotlib.pyplot as plt
        # Importação explícita do módulo de formatação para corrigir o aviso do Pylance
        import matplotlib.ticker as ticker

        # Ativa um estilo visual mais limpo e moderno
        plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

        # Cria a figura com proporções elegantes (Largura x Altura)
        fig, ax = plt.subplots(figsize=(8, 5))

        categorias = ['Capital Inicial', 'Juros Ganhos', 'Montante Final']
        # Calculando o capital inicial para fins de linha evolutiva básica
        capital_inicial = self.montante_final - self.total_juros_ganhos
        valores = [capital_inicial, self.total_juros_ganhos, self.montante_final]

        # 1. Plota a linha principal de evolução
        ax.plot(categorias, valores, color='#2ecc71', marker='o', linewidth=3, markersize=8, label='Evolução do Patrimônio')

        # 2. Cria um preenchimento sutil abaixo da linha (efeito área/gradiente)
        ax.fill_between(categorias, valores, color='#2ecc71', alpha=0.15)

        # 3. Customização de Títulos e Rótulos (Fontes limpas e sem poluição)
        ax.set_title("Projeção e Crescimento do Capital", fontsize=14, pad=15, fontweight='bold', color='#2c3e50')
        ax.set_ylabel("Valores (R$)", fontsize=11, labelpad=10, color='#34495e')
        
        # 4. Formatação corrigida utilizando o módulo oficial 'ticker'
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, loc: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")))

        # 5. Adiciona rótulos de dados diretamente no topo de cada ponto
        for i, v in enumerate(valores):
            v_formatado = f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            ax.annotate(v_formatado, 
                        (categorias[i], valores[i]),
                        textcoords="offset points", 
                        xytext=(0,10), 
                        ha='center', 
                        fontsize=9, 
                        fontweight='bold',
                        color='#2c3e50')

        # 6. Suaviza as linhas de grade para não poluir o visual
        ax.grid(True, linestyle='--', alpha=0.5, color='#bdc3c7')
        
        # Remove bordas desnecessárias da janela do gráfico (Clean Design)
        for spine in ['top', 'right', 'left', 'bottom']:
            ax.spines[spine].set_visible(False)

        # Ajusta as margens para o texto não ser cortado
        plt.tight_layout()
        
        # Mostra o gráfico na tela
        plt.show()