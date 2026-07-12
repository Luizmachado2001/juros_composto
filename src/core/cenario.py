# src/core/cenario.py

class Cenario:
    def __init__(self, capital_inicial: float, aporte_mensal: float, taxa_anual: float, inflacao_anual: float, tempo_meses: int):
        self.capital_inicial = capital_inicial
        self.aporte_mensal = aporte_mensal
        self.taxa_anual = taxa_anual
        self.inflacao_anual = inflacao_anual  # <-- Nova propriedade
        self.tempo_meses = tempo_meses