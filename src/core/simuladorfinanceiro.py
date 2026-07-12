# src/core/simuladorfinanceiro.py
from src.core.cenario import Cenario
from src.core.resultado import Resultado
from src.core.resultado_meta import ResultadoMeta

class SimuladorFinanceiro:
    # Constante de segurança para evitar loops infinitos (Equivalente a 100 anos)
    MAX_MESES = 1200

    def __init__(self):
        pass

    def calcular(self, cenario: Cenario) -> Resultado:
        # 1. Conversão exata da taxa anual para efetiva mensal
        taxa_mensal = (1 + (cenario.taxa_anual / 100)) ** (1 / 12) - 1
        fator_juros = 1 + taxa_mensal
        
        # Otimização: Guarda a potência calculada para reutilização na fórmula fechada
        fator_acumulado = fator_juros ** cenario.tempo_meses
        
        # 2. Cálculo do Montante Bruto usando a fórmula fechada da Série Geométrica - O(1)
        # Premissa: Aportes realizados ao final de cada mês (anuidade postecipada)
        capital_padrao = cenario.capital_inicial * fator_acumulado
        
        if taxa_mensal > 0:
            aportes_acumulados = cenario.aporte_mensal * ((fator_acumulado - 1) / taxa_mensal)
        else:
            aportes_acumulados = cenario.aporte_mensal * cenario.tempo_meses
            
        montante_bruto = capital_padrao + aportes_acumulados
        
        # 3. Contabilidade dos agregados monetários
        total_investido = cenario.capital_inicial + (cenario.aporte_mensal * cenario.tempo_meses)
        total_juros = montante_bruto - total_investido
                 
        # 4. Desconto geométrico da Inflação (Poder de Compra Real)
        inflacao_mensal = (1 + (cenario.inflacao_anual / 100)) ** (1 / 12) - 1
        fator_inflacao_acumulado = (1 + inflacao_mensal) ** cenario.tempo_meses
        montante_real = montante_bruto / fator_inflacao_acumulado
                 
        return Resultado(
            total_investido=total_investido,
            total_juros=total_juros,
            montante_final=montante_bruto,
            poder_compra_real=montante_real
        )

    # ================= CÁLCULO ATÉ O ALVO (ENGENHARIA REVERSA) =================
    def calcular_tempo_ate_alvo(self, capital: float, aporte: float, taxa_anual: float, inflacao_anual: float, alvo: float) -> ResultadoMeta:
        # 1. Preparação dos fatores mensais de juros e inflação
        taxa_mensal = (1 + (taxa_anual / 100)) ** (1 / 12) - 1
        inflacao_mensal = (1 + (inflacao_anual / 100)) ** (1 / 12) - 1
        
        fator_juros = 1 + taxa_mensal
        fator_inflacao = 1 + inflacao_mensal
        
        # 2. Inicialização das variáveis de controle
        montante_bruto = capital
        total_investido = capital
        fator_inflacao_acumulado = 1.0
        meses = 0
        
        # 3. Laço de simulação temporal
        # Premissa: Aportes realizados ao final de cada mês (anuidade postecipada)
        while True:
            montante_real = montante_bruto / fator_inflacao_acumulado
            
            # Condição de parada baseada na meta real ou no limite estrito de segurança
            if montante_real >= alvo or meses >= self.MAX_MESES:
                break
                
            meses += 1
            # Aplica os juros e injeta o aporte subsequente
            montante_bruto = (montante_bruto * fator_juros) + aporte
            total_investido += aporte
            
            # Atualização cumulativa da inflação para otimização interna
            fator_inflacao_acumulado *= fator_inflacao

        total_juros = montante_bruto - total_investido
        
        # 4. Tradução do tempo para formato legível de texto
        anos = meses // 12
        meses_restantes = meses % 12
        
        tempo_texto = ""
        if anos > 0:
            tempo_texto += f"{anos} ano{'s' if anos > 1 else ''}"
        if meses_restantes > 0:
            if tempo_texto:
                tempo_texto += " e "
            tempo_texto += f"{meses_restantes} mês{'es' if meses_restantes > 1 else ''}"
            
        if meses == 0 or (meses == self.MAX_MESES and montante_real < alvo):
            tempo_texto = "Prazo indefinido (+100 anos)" if meses == self.MAX_MESES else "Imediato"

        # Retorno padronizado utilizando objeto fortemente tipado
        return ResultadoMeta(
            meses_totais=meses,
            tempo_texto=tempo_texto,
            total_investido=total_investido,
            total_juros=total_juros,
            montante_final=montante_bruto,
            poder_compra_real=montante_real
        )