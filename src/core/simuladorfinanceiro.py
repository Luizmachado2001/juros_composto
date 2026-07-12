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
        inflacao_mensal = (1 + (cenario.inflacao_anual / 100)) ** (1 / 12) - 1
        fator_inflacao = (1 + inflacao_mensal) ** cenario.tempo_meses
                 
        montante_real = montante_bruto / fator_inflacao
                 
        return Resultado(
            total_investido=total_investido,
            total_juros=total_juros,
            montante_final=montante_bruto,
            poder_compra_real=montante_real
        )

    # ================= FUNÇÃO: CALCULAR O TEMPO ATÉ O ALVO =================
    def calcular_tempo_ate_alvo(self, capital: float, aporte: float, taxa_anual: float, inflacao_anual: float, alvo: float):
        taxa_mensal = (1 + (taxa_anual / 100)) ** (1 / 12) - 1
        inflacao_mensal = (1 + (inflacao_anual / 100)) ** (1 / 12) - 1
        
        montante_bruto = capital
        total_investido = capital
        meses = 0
        
        # O loop roda calculando o rendimento real descontando a inflação acumulada
        while montante_bruto / ((1 + inflacao_mensal) ** meses) < alvo and meses < 1200:
            meses += 1
            montante_bruto = montante_bruto * (1 + taxa_mensal)
            montante_bruto += aporte
            total_investido += aporte

        fator_inflacao = (1 + inflacao_mensal) ** meses
        montante_real = montante_bruto / fator_inflacao
        total_juros = montante_bruto - total_investido
        
        anos = meses // 12
        meses_restantes = meses % 12
        
        tempo_texto = ""
        if anos > 0:
            tempo_texto += f"{anos} ano{'s' if anos > 1 else ''}"
        if meses_restantes > 0:
            if tempo_texto:
                tempo_texto += " e "
            tempo_texto += f"{meses_restantes} mêt{'es' if meses_restantes > 1 else ''}"
        if meses == 0 or (meses == 1200 and montante_real < alvo):
            tempo_texto = "Prazo indefinido (+100 anos)" if meses == 1200 else "Imediato"

        return {
            "meses_totais": meses,
            "tempo_texto": tempo_texto,
            "total_investido": total_investido,
            "total_juros": total_juros,
            "montante_final": montante_bruto,
            "poder_compra_real": montante_real
        }