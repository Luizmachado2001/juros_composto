from .src import Cenario, SimuladorFinanceiro

def main():
    primeiro = Cenario(100000, 1.2, 12)
    
    SimuladorFinanceiro.tempoAteAlvo(primeiro, 1000000)
    calculo = SimuladorFinanceiro.calcularMontante(primeiro)
    calculo.exibirResumo()
    

if __name__ == "__main__":
    main()