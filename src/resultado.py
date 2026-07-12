from typing import Optional, List
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

class Resultado:
    """Representa o resultado final consolidado de uma simulação financeira.

    Esta classe armazena os valores finais acumulados, o lucro em juros, 
    e opcionalmente o histórico passo a passo para renderização de gráficos 
    de evolução patrimonial.

    Attributes:
        montante_final (float): O valor total acumulado (poder de compra real).
        total_juros_ganhos (float): O lucro puro em juros reais.
        historico_meses (list[int]): Lista opcional com os índices dos meses (para gráfico).
        historico_saldos (list[float]): Lista opcional com os saldos mês a mês (para gráfico).
    """

    def __init__(
        self, 
        montante_final: float, 
        total_juros_ganhos: float, 
        historico_meses: Optional[List[int]] = None, 
        historico_saldos: Optional[List[float]] = None
    ):
        """Inicializa um objeto Resultado com tipagem opcional estrita (PEP 484).

        Args:
            montante_final (float): O montante final acumulado (R$).
            total_juros_ganhos (float): O total de juros reais ganhos (R$).
            historico_meses (list[int], optional): Lista de meses para o gráfico. Defaults to None.
            historico_saldos (list[float], optional): Lista de saldos para o gráfico. Defaults to None.
        """
        self.montante_final = montante_final
        self.total_juros_ganhos = total_juros_ganhos
        
        # Garante que as listas sejam listas vazias se None for passado, 
        # mantendo a consistência do tipo para o restante da classe.
        self.historico_meses: List[int] = historico_meses or []
        self.historico_saldos: List[float] = historico_saldos or []

    def exibirResumo(self):
        """Dispara a exibição da interface gráfica se houver histórico de dados.

        Este método verifica se as listas de histórico foram preenchidas (não estão vazias).
        Se preenchidas, assume-se que o cálculo gerou uma evolução temporal compatível 
        com um gráfico de linha.
        """
        if self.historico_meses and self.historico_saldos:
            self.mostrarGraficoLinha()

    def mostrarGraficoLinha(self):
        """Gera um gráfico de linha elegante mostrando a curva exponencial do patrimônio.
        
        Este gráfico utiliza formatação profissional do Matplotlib para exibir a evolução 
        real do poder de compra ao longo do tempo.
        """
        # Configuração de tema limpo e profissional
        plt.style.use('default')
        fig, ax = plt.subplots(figsize=(8, 5), facecolor='#ffffff')
        ax.set_facecolor('#f8f9fa')  # Fundo levemente cinza para destacar a linha

        # Linha principal do Patrimônio
        ax.plot(self.historico_meses, self.historico_saldos, color='#00b4d8', linewidth=2.5, label='Evolução do Patrimônio Real')
        
        # Linha estável do Capital Inicial do bolso (Tracejada)
        capital_inicial = self.montante_final - self.total_juros_ganhos
        ax.axhline(y=capital_inicial, color='#e63946', linestyle='--', linewidth=1.5, label='Capital Investido Inicial')

        # Customização de Títulos e Eixos
        ax.set_title("A Curva Exponencial do seu Dinheiro (Descontada a Inflação)", fontsize=12, pad=20, fontweight='bold', color='#1d3557')
        ax.set_xlabel("Tempo (Meses)", fontsize=10, labelpad=10, color='#1d3557')
        ax.set_ylabel("Poder de Compra Real", fontsize=10, labelpad=10, color='#1d3557')
        
        # Formatação do eixo Y para o padrão R$ brasileiro (milhares/decimais)
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, loc: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")))
        ax.tick_params(colors='#4a4a4a', labelsize=9)

        # Destaca o ponto final da linha com uma bolinha e o valor escrito (anotação)
        ax.scatter(self.historico_meses[-1], self.historico_saldos[-1], color='#0077b6', s=50, zorder=5)
        v_final_formatado = f"R$ {self.montante_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        ax.annotate(v_final_formatado,
                    xy=(self.historico_meses[-1], self.historico_saldos[-1]),
                    xytext=(-15, 12),  
                    textcoords="offset points",
                    ha='right', va='bottom', fontsize=10, fontweight='bold', color='#0077b6',
                    bbox=dict(boxstyle="round,pad=0.3", fc="#e2eafc", ec="none", alpha=0.8))

        # Estética das grades e legendas
        ax.grid(True, linestyle=':', alpha=0.6, color='#b2b2b2')
        ax.legend(loc='upper left', frameon=True, facecolor='#ffffff', edgecolor='none', fontsize=9)
        
        # Oculta as bordas (spines) externa do gráfico
        for spine in ['top', 'right', 'left', 'bottom']:
            ax.spines[spine].set_visible(False)

        plt.tight_layout()
        plt.show()