from .src import Cenario, SimuladorFinanceiro

def main():
    
    primeiro = Cenario(1000, 1.2, 200)
    
    SimuladorFinanceiro.simular_juros_compostos_com_aportes(primeiro, 100, 10000)
    SimuladorFinanceiro.tempoAteAlvo(primeiro, 10000)
    calculo = SimuladorFinanceiro.calcularMontante(primeiro)
    calculo.exibirResumo()
    

if __name__ == "__main__":
    main()