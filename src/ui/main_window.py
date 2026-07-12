# src/ui/main_window.py
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QLineEdit, QPushButton, QFrame, QMessageBox, QScrollArea
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QDoubleValidator, QIntValidator

from src.core.simuladorfinanceiro import SimuladorFinanceiro
from src.core.cenario import Cenario
from src.core.resultado import Resultado

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulador Financeiro")
        
        self.setMinimumSize(1020, 720)
        self.resize(1080, 760)
        
        # UI Avançada: Botão Holográfico/Cyberpunk com transição de bordas e preenchimento dinâmico
        self.setStyleSheet("""
            QMainWindow {
                background-color: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #070913, 
                    stop: 0.5 #0f1322,
                    stop: 1 #05060b
                );
            }
            QLabel {
                color: #94a3b8;
                font-family: 'Segoe UI', system-ui, sans-serif;
                font-size: 13px;
            }
            QLineEdit {
                background-color: #131927;
                border: 1px solid #222f47;
                border-radius: 6px;
                color: #f8fafc;
                padding: 13px 16px;
                font-size: 15px;
                font-family: 'Segoe UI', sans-serif;
            }
            QLineEdit:focus {
                border: 1px solid #00f2fe; /* Foco em Ciano Neon */
                background-color: #0b0f19;
            }
            QLineEdit::placeholder {
                color: #334155;
            }
            
            /* ================= BOTÃO TECNOLÓGICO HOLOGRÁFICO ================= */
            QPushButton {
                background-color: rgba(0, 242, 254, 0.05); /* Fundo quase transparente */
                color: #00f2fe;                             /* Texto ciano neon */
                border: 2px solid #00f2fe;                  /* Borda brilhante sólida */
                border-radius: 4px;                         /* Cantos retos e sofisticados */
                padding: 15px;
                font-size: 14px;
                font-family: 'Segoe UI', sans-serif;
                font-weight: 800;
                text-transform: uppercase;
                letter-spacing: 2px;                        /* Espaçamento futurista de letras */
                margin-top: 35px;
            }
            QPushButton:hover {
                background-color: #00f2fe;                  /* Preenche o botão ao passar o mouse */
                color: #05070f;                             /* Inverte a cor do texto para contraste */
                border: 2px solid #00f2fe;
            }
            QPushButton:pressed {
                background-color: #00b8c4;
                border: 2px solid #00b8c4;
            }
            
            QFrame#card_resultado {
                background-color: #0b0f19;
                border-radius: 12px;
                border: 1px solid #1e293b;
            }
            QScrollArea { 
                border: none; 
                background-color: transparent; 
            }
        """)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(50, 50, 50, 50)
        self.main_layout.setSpacing(70)

        # ------------------ PAINEL ESQUERDO (INPUTS) ------------------
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_widget.setStyleSheet("background-color: transparent;")
        self.layout_esquerdo = QVBoxLayout(self.scroll_widget)
        self.layout_esquerdo.setContentsMargins(0, 0, 20, 0)
        self.scroll_area.setWidget(self.scroll_widget)
        
        self.main_layout.addWidget(self.scroll_area, stretch=1)

        # Título atualizado para português
        titulo_inputs = QLabel("Dados da Simulação")
        titulo_inputs.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
        titulo_inputs.setStyleSheet("color: #ffffff; margin-bottom: 30px; letter-spacing: 0.5px; font-weight: 800;")
        self.layout_esquerdo.addWidget(titulo_inputs)

        self.input_capital = self.criar_campo_entrada("Capital Inicial", "R$ 0,00", real=True)
        self.input_aporte = self.criar_campo_entrada("Aporte Mensal", "R$ 0,00", real=True)
        self.input_taxa = self.criar_campo_entrada("Taxa de Juros Anual", "0.00 %", real=True)
        self.input_inflacao = self.criar_campo_entrada("Taxa de Inflação Anual", "0.00 %", real=True)
        self.input_tempo = self.criar_campo_entrada("Período de Tempo", "Meses desejados", real=False)

        self.botao_calcular = QPushButton("Executar Simulação")
        self.botao_calcular.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_calcular.clicked.connect(self.processar_simulacao)
        self.layout_esquerdo.addWidget(self.botao_calcular)
        self.layout_esquerdo.addStretch()

        # ------------------ PAINEL DIREITO (RESULTADOS) ------------------
        self.layout_direito = QVBoxLayout()
        self.main_layout.addLayout(self.layout_direito, stretch=1)

        self.card_resultado = QFrame()
        self.card_resultado.setObjectName("card_resultado")
        self.card_layout = QVBoxLayout(self.card_resultado)
        self.card_layout.setContentsMargins(45, 45, 45, 45)
        self.card_layout.setSpacing(28)

        # Título atualizado para português
        titulo_resultados = QLabel("Projeção de Rendimento")
        titulo_resultados.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        titulo_resultados.setStyleSheet("color: #ffffff; margin-bottom: 15px; letter-spacing: 0.5px; font-weight: 800;")
        self.card_layout.addWidget(titulo_resultados)

        self.lbl_total_investido = self.criar_campo_resultado("Total Investido")
        self.lbl_total_juros = self.criar_campo_resultado("Rendimentos Brutos")
        self.lbl_montante_final = self.criar_campo_resultado("Montante Acumulado")
        
        divisor = QFrame()
        divisor.setFrameShape(QFrame.Shape.HLine)
        divisor.setStyleSheet("background-color: #1e293b; max-height: 1px; margin: 15px 0px;")
        self.card_layout.addWidget(divisor)

        self.lbl_poder_compra = self.criar_campo_resultado("Poder de Compra Real\n(Ajustado à Inflação)", destacado=True)

        self.layout_direito.addWidget(self.card_resultado)
        self.layout_direito.addStretch()

    def criar_campo_entrada(self, label_text, placeholder, real=True):
        container = QVBoxLayout()
        container.setSpacing(8)
        
        label = QLabel(label_text)
        label.setStyleSheet("font-weight: 700; color: #475569; font-size: 11px; text-transform: uppercase; letter-spacing: 1px;")
        
        line_edit = QLineEdit()
        line_edit.setPlaceholderText(placeholder)
        line_edit.setMinimumHeight(46)
        
        if real:
            validador = QDoubleValidator(0.0, 999999999.0, 2)
            validador.setNotation(QDoubleValidator.Notation.StandardNotation)
            line_edit.setValidator(validador)
        else:
            line_edit.setValidator(QIntValidator(1, 1200))
            
        container.addWidget(label)
        container.addWidget(line_edit)
        container.setContentsMargins(0, 0, 0, 15)
        self.layout_esquerdo.addLayout(container)
        return line_edit

    def criar_campo_resultado(self, label_text, destacado=False):
        container = QHBoxLayout()
        lbl_nome = QLabel(label_text)
        lbl_valor = QLabel("R$ 0,00")
        
        if destacado:
            lbl_nome.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
            lbl_nome.setStyleSheet("color: #f8fafc; letter-spacing: 0.5px;")
            lbl_valor.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
            lbl_valor.setStyleSheet("color: #00f2fe;") 
        else:
            lbl_nome.setStyleSheet("color: #475569; font-weight: 600; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px;")
            lbl_valor.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
            lbl_valor.setStyleSheet("color: #e2e8f0;")
            
        container.addWidget(lbl_nome)
        container.addStretch()
        container.addWidget(lbl_valor)
        self.card_layout.addLayout(container)
        return lbl_valor

    def formatar_moeda(self, valor: float) -> str:
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    def processar_simulacao(self):
        try:
            capital = float(self.input_capital.text().replace(",", ".")) if self.input_capital.text() else 0.0
            aporte = float(self.input_aporte.text().replace(",", ".")) if self.input_aporte.text() else 0.0
            taxa = float(self.input_taxa.text().replace(",", ".")) if self.input_taxa.text() else 0.0
            inflacao = float(self.input_inflacao.text().replace(",", ".")) if self.input_inflacao.text() else 0.0
            tempo = int(self.input_tempo.text()) if self.input_tempo.text() else 0

            if tempo <= 0:
                QMessageBox.warning(self, "Aviso", "Por favor, insira um período válido em meses.")
                return

            cenario = Cenario(capital, aporte, taxa, inflacao, tempo)
            simulador = SimuladorFinanceiro()
            
            resultado_calculado: Resultado = simulador.calcular(cenario)
            
            self.lbl_total_investido.setText(self.formatar_moeda(resultado_calculado.total_investido))
            self.lbl_total_juros.setText(self.formatar_moeda(resultado_calculado.total_juros))
            self.lbl_montante_final.setText(self.formatar_moeda(resultado_calculado.montante_final))
            self.lbl_poder_compra.setText(self.formatar_moeda(resultado_calculado.poder_compra_real))

        except Exception as e:
            QMessageBox.critical(self, "Erro no Cálculo", f"Ocorreu um erro ao processar a simulação: {str(e)}")