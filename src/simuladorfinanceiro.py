from .resultado import Resultado

class SimuladorFinanceiro():

    @staticmethod
    def calcularMontante(cenario) -> Resultado:
        p = cenario.getValorInicial()
        i = cenario.getTaxaJurosMensal()
        t = cenario.getTempoMeses()

        primeiro_passo = (i / 100)
        primeiro_passo = (primeiro_passo + 1) ** t

        segundo_passo = p * primeiro_passo

        montante_final = segundo_passo

        return Resultado(montante_final, montante_final-p)
    
    @staticmethod
    def tempoAteAlvo(cenario, alvo) -> int:
        montante_atual = cenario.getValorInicial()
        i = cenario.getTaxaJurosMensal() / 100
        meses = 0

        while (montante_atual < alvo):
            juros_do_mes = montante_atual * i
            montante_atual+=juros_do_mes
            meses+=1

            valor_formatado = f"{montante_atual:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            print(f"Mês: {meses:02d} | Valor acumulado: R$ {valor_formatado}")
            
        return meses
