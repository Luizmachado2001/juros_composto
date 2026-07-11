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

        anos = int(meses / 12)
        resto = meses % 12

        print(35 * "-")
        print("🎯 ALVO ATINGIDO!")
        if resto >= 1:
            print(f"Tempo total: {anos} ano(s) e {resto} mês(es)")
        else:
            print(f"Tempo total: {anos} ano(s)")

        print(35 * "-")
        print()
        return meses

    @staticmethod
    def simular_juros_compostos_com_aportes(cenario, aporte_mensal, alvo):
        """
        Simula a evolução mensal de um investimento com aportes até atingir um valor alvo.

        Este método projeta mês a mês o crescimento do patrimônio aplicando a taxa de
        juros sobre o saldo acumulado e somando o aporte mensal, exibindo o progresso
        no terminal até que o montante final seja igual ou maior que a meta definida.

        Args:
            cenario (Cenario): Objeto que contém as configurações iniciais da simulação
                (deve implementar getValorInicial() e getTaxaJurosMensal()).
            aporte_mensal (float): O valor financeiro depositado mensalmente.
            alvo (float): O montante final desejado (meta financeira).

        Returns:
            int: O total de meses necessários para atingir ou ultrapassar o valor alvo.

        Raises:
            ValueError: Se o valor inicial e o aporte forem zero com um alvo maior que zero,
                ou se a taxa de juros for negativa/nula impedindo o crescimento.
        """
        montante_atual = cenario.getValorInicial()
        i = cenario.getTaxaJurosMensal() / 100
        meses = 0

        while (montante_atual < alvo):
            juros_do_mes = montante_atual * i
            montante_atual+=juros_do_mes
            montante_atual+=aporte_mensal
            meses+=1

            valor_formatado = f"{montante_atual:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

            print(f"Mês: {meses:02d} | Valor acumulado: R$ {valor_formatado}")

        anos = int(meses / 12)
        resto = meses % 12

        print(35 * "-")
        print("🎯 ALVO ATINGIDO!")
        if resto >= 1:
            print(f"Tempo total: {anos} ano(s) e {resto} mês(es)")
        else:
            print(f"Tempo total: {anos} ano(s)")

        print(35 * "-")
        print()
        return meses
