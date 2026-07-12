# src/core/simuladorfinanceiro.py
from src.core.cenario import Cenario
from src.core.resultado import Resultado

class SimuladorFinanceiro:
    def __init__(self):
        pass

    def calcular(self, cenario: Cenario) -> Resultado:
        # 1. Cálculos Brutos (Sem inflação)
        taxa_mensal = (1 + (cenario.taxa_anual / 100)) ** (1 / 12) - 1
        total_investido = cenario.capital_inicial + (cenario.aporte_mensal * cenario.tempo_meses)
        
        montante_bruto = cenario.capital_inicial * ((1 + taxa_mensal) ** cenario.tempo_meses)
        for i in range(1, cenario.tempo_meses + 1):
            montante_bruto += cenario.aporte_mensal * ((1 + taxa_mensal) ** (cenario.tempo_meses - i))
            
        total_juros = montante_bruto - total_investido
        
        # 2. Desconto da Inflação (Poder de Compra Real)
        # Transforma a inflação anual em mensal e calcula o efeito cumulativo
        inflacao_mensal = (1 + (cenario.inflacao_anual / 100)) ** (1 / 12) - 1
        fator_inflacao = (1 + inflacao_mensal) ** cenario.tempo_meses
        
        # O montante real é o montante bruto dividido pelo quanto a inflação cresceu no período
        montante_real = montante_bruto / fator_inflacao
        
        return Resultado(
            total_investido=total_investido,
            total_juros=total_juros,
            montante_final=montante_bruto,
            poder_compra_real=montante_real  # <-- Enviando o valor com inflação descontada
        )