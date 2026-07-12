from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich import box
from .cenario import Cenario
from .resultado import Resultado

class SimuladorFinanceiro:
    """Motor de cálculo financeiro responsável pelas projeções e formatação no terminal."""

    @staticmethod
    def _formatar_moeda(valor: float) -> str:
        """Auxiliar para formatar valores numéricos no padrão de moeda brasileiro R$."""
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    @staticmethod
    def _formatar_tempo(meses: int) -> str:
        """Converte uma contagem de meses bruta em uma string legível de anos e meses."""
        if meses == 0:
            return "Início"
        anos = meses // 12
        meses_restantes = meses % 12
        
        partes = []
        if anos > 0:
            partes.append(f"{anos} ano{'s' if anos > 1 else ''}")
        if meses_restantes > 0:
            partes.append(f"{meses_restantes} mê{'ses' if meses_restantes > 1 else 's'}")
            
        return " e ".join(partes)

    @staticmethod
    def calcularMontante(cenario: Cenario, inflacao_mensal: float = 0.35) -> Resultado:
        """Calcula o montante fixo do cenário descontando a inflação pela fórmula de Fisher."""
        p = cenario.getValorInicial()
        i_nominal = cenario.getTaxaJurosMensal()
        t = cenario.getTempoMeses()

        i_real = (((1 + i_nominal / 100) / (1 + inflacao_mensal / 100)) - 1)

        historico_meses = list(range(t + 1))
        historico_saldos = [p * ((1 + i_real) ** m) for m in historico_meses]

        montante_real = historico_saldos[-1]
        juros_reais = montante_real - p

        # Exibição executiva do resumo fixo diretamente no terminal
        console = Console()
        
        v_inicial_f = SimuladorFinanceiro._formatar_moeda(p)
        v_final_f = SimuladorFinanceiro._formatar_moeda(montante_real)
        juros_f = SimuladorFinanceiro._formatar_moeda(juros_reais)
        
        # Painel lateral clean e moderno para o sumário de dados
        paineis = [
            Panel(f"[dim]Aporte Inicial[/dim]\n[bold white]{v_inicial_f}[/bold white]", border_style="dim"),
            Panel(f"[dim]Rendimento Real Total[/dim]\n[bold gold3]{juros_f}[/bold gold3]", border_style="dim"),
            Panel(f"[dim]Poder de Compra Final[/dim]\n[bold green]{v_final_f}[/bold green]", border_style="green")
        ]
        
        console.print("\n[bold white]EXTRATO DE PROJEÇÃO REAL PATRIMONIAL[/bold white]")
        console.print(f"[dim]Horizonte temporal: {SimuladorFinanceiro._formatar_tempo(t)} | Taxa real calculada: {i_real*100:.4f}% ao mês[/dim]\n")
        console.print(Columns(paineis))
        console.print("")

        return Resultado(montante_real, juros_reais, historico_meses, historico_saldos)

    @staticmethod
    def tempoAteAlvo(cenario: Cenario, alvo: float, inflacao_mensal: float = 0.35) -> int:
        """Calcula o tempo sem aportes com uma tabela executiva minimalista."""
        console = Console()
        montante_atual = cenario.getValorInicial()
        i_nominal = cenario.getTaxaJurosMensal()
        i_real = (((1 + i_nominal / 100) / (1 + inflacao_mensal / 100)) - 1)
        meses = 0

        tabela = Table(
            title=f"\n[bold white]CRONOGRAMA DE EVOLUÇÃO ATÉ O ALVO[/bold white]\n[dim]Alvo em poder de compra de hoje: {SimuladorFinanceiro._formatar_moeda(alvo)}[/dim]",
            title_justify="left",
            box=box.MINIMAL,
            header_style="bold steel_blue1",
            show_lines=False
        )
        tabela.add_column("Período Decorrido", justify="left", width=25)
        tabela.add_column("Saldo Real Corrigido", justify="right", style="bold green", width=25)

        tabela.add_row(
            SimuladorFinanceiro._formatar_tempo(meses), 
            SimuladorFinanceiro._formatar_moeda(montante_atual)
        )

        while montante_atual < alvo:
            meses += 1
            montante_atual += (montante_atual * i_real)
            
            # Print anualizado ou do fechamento do alvo
            if meses % 12 == 0 or montante_atual >= alvo:
                tabela.add_row(
                    SimuladorFinanceiro._formatar_tempo(meses), 
                    SimuladorFinanceiro._formatar_moeda(montante_atual)
                )
                
            if meses >= 1200: 
                break

        console.print(tabela)
        console.print("")
        return meses

    @staticmethod
    def simular_juros_compostos_com_aportes(cenario: Cenario, aporte_mensal: float, alvo: float, inflacao_mensal: float = 0.35) -> int:
        """Simula a evolução real com aportes periódicos exibindo tabela limpa e corporativa."""
        console = Console()
        montante_atual = cenario.getValorInicial()
        i_nominal = cenario.getTaxaJurosMensal()
        i_real = (((1 + i_nominal / 100) / (1 + inflacao_mensal / 100)) - 1)
        meses = 0

        tabela = Table(
            title=f"\n[bold white]EFEITO DOS APORTES MENSAIS RECORRENTES[/bold white]\n[dim]Aporte mensal contínuo: {SimuladorFinanceiro._formatar_moeda(aporte_mensal)}[/dim]",
            title_justify="left",
            box=box.MINIMAL,
            header_style="bold plum1",
            show_lines=False
        )
        tabela.add_column("Período Decorrido", justify="left", width=25)
        tabela.add_column("Saldo Real Acumulado", justify="right", style="bold green", width=25)

        tabela.add_row(
            SimuladorFinanceiro._formatar_tempo(meses), 
            SimuladorFinanceiro._formatar_moeda(montante_atual)
        )

        while montante_atual < alvo:
            meses += 1
            montante_atual += (montante_atual * i_real) + aporte_mensal
            
            if meses % 12 == 0 or montante_atual >= alvo:
                tabela.add_row(
                    SimuladorFinanceiro._formatar_tempo(meses), 
                    SimuladorFinanceiro._formatar_moeda(montante_atual)
                )

            if meses >= 1200:
                break

        console.print(tabela)
        console.print("")
        return meses