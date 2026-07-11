from .resultado import Resultado
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box  # Importado para melhorar o estilo das bordas das tabelas

# Inicializa o console global do Rich
console = Console()

class SimuladorFinanceiro():
    """
    Mecanismo de cálculo para operações financeiras de juros compostos.

    Esta classe fornece métodos estáticos utilitários para simular o crescimento
    de capital ao longo do tempo e calcular projeções com base em metas financeiras.
    Não necessita de instanciação.
    """

    @staticmethod
    def calcularMontante(cenario) -> Resultado:
        """
        Calcula o montante final acumulado e o total de juros com base em um cenário.
        """
        p = cenario.getValorInicial()
        i = cenario.getTaxaJurosMensal()
        t = cenario.getTempoMeses()

        primeiro_passo = (i / 100)
        primeiro_passo = (primeiro_passo + 1) ** t

        segundo_passo = p * primeiro_passo
        montante_final = segundo_passo

        return Resultado(montante_final, montante_final - p)
    
    @staticmethod
    def tempoAteAlvo(cenario, alvo) -> int:
        """
        Simula la evolución mensual del capital hasta alcanzar o superar el valor objetivo.
        Incluye la columna de intereses acumulados y diseño de tabla mejorado.
        """
        valor_inicial = cenario.getValorInicial()
        montante_atual = valor_inicial
        i = cenario.getTaxaJurosMensal() / 100
        meses = 0

        # Tabela melhorada com bordas arredondadas e estilo clean
        tabela = Table(
            title="[bold magenta]Evolução do Patrimônio (Sem Aportes)[/bold magenta]", 
            show_header=True, 
            header_style="bold cyan",
            box=box.ROUNDED,
            border_style="dim"
        )
        tabela.add_column("Mês", justify="center", style="dim")
        tabela.add_column("Valor Acumulado", justify="right", style="green")
        tabela.add_column("Juros Acumulados", justify="right", style="yellow")  # Nova coluna!

        while (montante_atual < alvo):
            juros_do_mes = montante_atual * i
            montante_atual += juros_do_mes
            meses += 1

            # Juros acumulados sem aporte é apenas o montante atual menos o que começou
            juros_acumulado = montante_atual - valor_inicial

            valor_formatado = f"R$ {montante_atual:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            juros_formatado = f"R$ {juros_acumulado:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            
            tabela.add_row(f"{meses:02d}", valor_formatado, juros_formatado)

        console.print(tabela)

        anos = int(meses / 12)
        resto = meses % 12

        tempo_texto = f"{anos} ano(s) e {resto} mês(es)" if resto >= 1 else f"{anos} ano(s)"
        painel_sucesso = Panel(
            Text(f"Tempo total necessário: {tempo_texto}", style="bold white"),
            title="[bold green]🎯 ALVO ATINGIDO![/bold green]",
            expand=False,
            border_style="green"
        )
        console.print("\n", painel_sucesso, "\n")
        
        return meses

    @staticmethod
    def simular_juros_compostos_com_aportes(cenario, aporte_mensal, alvo) -> int:
        """
        Simula la evolución mensual de una inversión con aportes hasta alcanzar un valor objetivo.
        Diseño de tabla mejorado.
        """
        montante_atual = cenario.getValorInicial()
        total_investido_bolso = cenario.getValorInicial()  
        i = cenario.getTaxaJurosMensal() / 100
        meses = 0

        # Tabela melhorada com bordas arredondadas e estilo clean
        tabela = Table(
            title="[bold violet]Evolução do Patrimônio (Com Aportes Mensais)[/bold violet]", 
            show_header=True, 
            header_style="bold cyan",
            box=box.ROUNDED,
            border_style="dim"
        )
        tabela.add_column("Mês", justify="center", style="dim")
        tabela.add_column("Valor Acumulado", justify="right", style="green")
        tabela.add_column("Juros Acumulados", justify="right", style="yellow")

        while (montante_atual < alvo):
            juros_do_mes = montante_atual * i
            montante_atual += juros_do_mes
            montante_atual += aporte_mensal
            
            total_investido_bolso += aporte_mensal
            meses += 1

            juros_acumulado = montante_atual - total_investido_bolso

            valor_formatado = f"R$ {montante_atual:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            juros_formatado = f"R$ {juros_acumulado:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

            tabela.add_row(f"{meses:02d}", valor_formatado, juros_formatado)

        console.print(tabela)

        anos = int(meses / 12)
        resto = meses % 12

        tempo_texto = f"{anos} ano(s) e {resto} mês(es)" if resto >= 1 else f"{anos} ano(s)"
        painel_sucesso = Panel(
            Text(f"Tempo total necessário: {tempo_texto}", style="bold white"),
            title="[bold gold1]🎯 ALVO ATINGIDO COM APORTES![/bold gold1]",
            expand=False,
            border_style="green"
        )
        console.print("\n", painel_sucesso, "\n")
        
        return meses