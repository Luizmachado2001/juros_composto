# 🌌 Simulador Financeiro - Juros Compostos & Inflação Real

Um simulador financeiro avançado com interface gráfica **Cyberpunk/Holográfica** desenvolvido em Python e PyQt6. O projeto calcula a evolução de investimentos baseada em juros compostos e realiza o desconto automático da inflação (Poder de Compra Real), utilizando a metodologia matemática de Fisher.

---

## 🚀 Funcionalidades Principais

O simulador opera em duas frentes inteligentes e integradas:

1. **Simular por Tempo (Projeção Tradicional):**
   * Você insere o capital inicial, aportes mensais, taxa de juros e inflação anual.
   * O sistema projeta exatamente quanto você terá acumulado em formato bruto (nominal) e o seu **Poder de Compra Real** equivalente ao dinheiro de hoje após o período de meses desejado.

2. **Calcular para Alvo (Engenharia Reversa de Metas):**
   * Você define um **Valor Alvo** que deseja alcançar (ex: R$ 1.000.000,00 em poder de compra de hoje).
   * O motor de cálculo simula mês a mês e descobre o **tempo exato em anos e meses** necessário para você bater a meta, considerando o peso da inflação corroendo o dinheiro ao longo dos anos.

---

## 📊 Arquitetura do Projeto

O software segue os padrões de arquitetura corporativa e separação de responsabilidades (Clean Code / MVC):

```text
juros_composto/
├── src/
│   ├── __main__.py          # Ponto de entrada da aplicação
│   ├── core/                # Motor de Cálculo e Regras de Negócio
│   │   ├── cenario.py       # Modelo para os dados de entrada
│   │   ├── resultado.py     # Modelo para encapsular os resultados
│   │   └── simuladorfinanceiro.py # Algoritmos de juros e inflação
│   └── ui/                  # Camada de Interface Gráfica
│       └── main_window.py   # Janela em PyQt6 com estilo Neon/Cyberpunk
