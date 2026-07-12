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
```

🎨 Design & Interface

A interface foi totalmente customizada através de folhas de estilo avançadas (QSS) para entregar uma experiência moderna:

    Fundo Gradiente Escuro: Paleta focada em tons de azul escuro e preto espacial.

    Foco Neon: Inputs com feedback visual dinâmico em Ciano Neon ao receberem clique.

    Painéis Simétricos: Divisão harmônica entre o bloco de formulário encapsulado e o card flutuante de resultados.

🛠️ Tecnologias Utilizadas```

    Python 3.14+

    PyQt6 (Interface Gráfica de Alta Performance)

    Pylance (Análise estática de tipos)

🏃‍♂️ Como Executar o Projeto
Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina e a biblioteca PyQt6.

    Clone o repositório:
    Bash

    git clone [https://github.com/luizmachado2001/juros_composto.git](https://github.com/luizmachado2001/juros_composto.git)
    cd juros_composto

    Instale as dependências:
    Bash

    pip install PyQt6

    Execute o simulador:
    Bash

    python -m src.__main__

📝 Exemplo Prático de Cálculo (Alvo)

Se você investir R$ 100.000,00 iniciais (sem aportes mensais) a uma taxa de 15% ao ano, com uma inflação de 4,50% ao ano, e estipular um Alvo de R$ 1.000.000,00:

    O sistema calculará que você precisa de exatamente 24 anos e 1 mês para alcançar o objetivo.

    Para garantir que você compre hoje o equivalente a R$ 1.000.000,00, o saldo nominal em sua conta no futuro precisará ser de R$ 2.896.051,78 (compensando a perda inflacionária do período).

Desenvolvido por Luiz Machado. 🌌
