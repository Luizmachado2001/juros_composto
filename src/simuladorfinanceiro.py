from .resultado import Resultado

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

        Utiliza a fórmula matemática de juros compostos: M = P * (1 + i)^t.

        Args:
            cenario (Cenario): Objeto contendo os dados de entrada (capital, taxa e tempo).

        Returns:
            Resultado: Um objeto contendo o montante final e o total de juros acumulados.
        """
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
        """
        Simula a evolução mensal do capital até atingir ou ultrapassar o valor alvo.

        Realiza projeções mês a mês aplicando juros compostos sobre o saldo acumulado.

        Args:
            cenario (Cenario): Objeto com os dados iniciais do investimento.
            alvo (float): O valor financeiro objetivo que se deseja alcançar.

        Returns:
            int: A quantidade total de meses necessários para atingir o alvo.
        """
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
