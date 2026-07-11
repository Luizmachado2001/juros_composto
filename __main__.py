from .src import Cenario, SimuladorFinanceiro
from rich.console import Console
from rich.rule import Rule

def main():
    # Inicializa o console para criar divisores bonitos entre os testes
    console = Console()
    
    # Instancia o cenário: R$ 1.000 iniciais, 1.2% de taxa mensal, por 200 meses
    primeiro = Cenario(100000, 1.2, 200)
    
    # --- SIMULAÇÃO 1: Meta Com Aportes ---
    console.print(Rule("[bold violet]1. Simulação Com Aportes Mensais[/bold violet]"))
    SimuladorFinanceiro.simular_juros_compostos_com_aportes(primeiro, 100, 1000000)
    
    # --- SIMULAÇÃO 2: Meta Sem Aportes ---
    console.print(Rule("[bold magenta]2. Simulação Sem Aportes (Apenas Juros)[/bold magenta]"))
    SimuladorFinanceiro.tempoAteAlvo(primeiro, 1000000)
    
    # --- SIMULAÇÃO 3: Cálculo Fixo e Resumo Visual ---
    console.print(Rule("[bold blue]3. Resumo Fixo do Cenário (200 meses)[/bold blue]"))
    calculo = SimuladorFinanceiro.calcularMontante(primeiro)
    calculo.exibirResumo() # Aqui ele vai mostrar o painel Rich e abrir o gráfico melhorado!

if __name__ == "__main__":
    main()