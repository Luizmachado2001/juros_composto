class Resultado:
    def __init__(self, montante_final, total_juros_ganhos):
        self.montante_final = montante_final
        self.total_juros_ganhos = total_juros_ganhos

    def exibirResumo(self):
        # Formatando os valores para o padrão BR antes de exibir
        montante_br = f"{self.montante_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        juros_br = f"{self.total_juros_ganhos:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        
        # Aumentamos o multiplicador para 35 para cobrir todo o texto elegantemente
        print(35 * "=")
        print("       RESUMO DO INVESTIMENTO     ")
        print(35 * "=")
        print(f"Montante Final:        R$ {montante_br}")
        print(f"Total de Juros Ganhos: R$ {juros_br}")
        print(35 * "=")