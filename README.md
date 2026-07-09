# 📈 Simulador de Juros Compostos

Um simulador financeiro modular desenvolvido em Python para calcular a evolução de investimentos baseados em juros compostos. O projeto aplica conceitos rigorosos de **Orientação a Objetos (POO)** e segue uma arquitetura inspirada no padrão MVC (Separação de Responsabilidades), garantindo que a lógica de cálculo, armazenamento de dados e exibição na tela fiquem em camadas totalmente independentes.

---

## 🚀 Funcionalidades

* **Cálculo de Montante:** Calcula o valor final acumulado e o total de juros ganhos com base em um cenário inicial (Capital, Taxa e Tempo).
* **Previsão de Tempo até o Alvo:** Simula mês a mês a evolução do capital até que ele atinja ou ultrapasse um valor de alvo estipulado pelo usuário.
* **Formatação Monetária PT-BR:** Exibição dos resultados no terminal totalmente formatada no padrão brasileiro (`R$ 1.112.455,41`).

---

## 🏗️ Arquitetura do Sistema

O projeto foi estruturado seguindo boas práticas de design de software, dividido em pacotes e classes com responsabilidades únicas:

| Classe | Responsabilidade | Tipo de Métodos |
| :--- | :--- | :--- |
| `Cenario` | Encapsula os dados de entrada do investimento (Capital Inicial, Taxa de Juros e Tempo). | Métodos de instância (Getters) |
| `SimuladorFinanceiro` | Contém as regras de negócio e fórmulas matemáticas de juros compostos. | Métodos Estáticos (`@staticmethod`) |
| `Resultado` | Armazena os dados calculados e gerencia a formatação visual/exibição no terminal. | Métodos de instância |

### Estrutura de Pastas
```text
juros_composto/
│
├── src/
│   ├── __init__.py           # Gerencia as exportações do pacote
│   ├── cenario.py            # Modelo de dados de entrada
│   ├── resultado.py          # Modelo de saída e exibição
│   └── simuladorfinanceiro.py # Lógica dos cálculos e simulação
│
└── __main__.py               # Ponto de entrada (Orquestrador do sistema)
