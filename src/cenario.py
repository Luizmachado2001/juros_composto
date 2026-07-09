class Cenario:
    def __init__(self, valor_inicial, taxa_juros_mensal, tempo_meses):
        self.valor_inicial = valor_inicial
        self.taxa_juros_mensal = taxa_juros_mensal
        self.tempo_meses = tempo_meses

    def getValorInicial(self) -> float:
        return self.valor_inicial
    
    def getTaxaJurosMensal(self) -> float:
        return self.taxa_juros_mensal
    
    def getTempoMeses(self) -> int:
        return self.tempo_meses