# src/core/resultado_meta.py

class ResultadoMeta:
    def __init__(self, meses_totais: int, tempo_texto: str, total_investido: float, total_juros: float, montante_final: float, poder_compra_real: float):
        self.meses_totais = meses_totais
        self.tempo_texto = tempo_texto
        self.total_investido = total_investido
        self.total_juros = total_juros
        self.montante_final = montante_final
        self.poder_compra_real = poder_compra_real