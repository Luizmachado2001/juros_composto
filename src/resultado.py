class Resultado:
    def __init__(self, montante_final, total_juros_ganhos):
        self.montante_final = montante_final
        self.total_juros_ganhos = total_juros_ganhos

    def exibirResumo(self) -> None:
        print(30 * "=")
        print("RESUMO DO INVESTIMENTO")
        print(f"Montante Final: {self.montante_final:.2f}")
        print(f"Total de Juros Ganhos: {self.total_juros_ganhos:.2f}")
        print(30 * "=")