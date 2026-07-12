# src/core/resultado.py

class Resultado:
    def __init__(self, total_investido: float, total_juros: float, montante_final: float, poder_compra_real: float):
        self.total_investido = total_investido
        self.total_juros = total_juros
        self.montante_final = montante_final
        self.poder_compra_real = poder_compra_real  # <-- Nova propriedade