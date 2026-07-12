# src/ui/main_window.py
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QLineEdit, QPushButton, QFrame, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QDoubleValidator, QIntValidator
from src.core.simuladorfinanceiro import SimuladorFinanceiro
from src.core.cenario import Cenario
from src.core.resultado import Resultado
from src.core.resultado_meta import ResultadoMeta

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulador Financeiro")
                 
        self.setMinimumSize(1050, 750)
        self.resize(1100, 780)
                 
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
                border: 1px solid #00f2fe; 
                background-color: #0b0f19;
            }
            QLineEdit::placeholder {
                color: #334155;
            }
                         
            QPushButton {
                background-color: rgba(0, 242, 254, 0.05); 
                color: #00f2fe;                             
                border: 2px solid #00f2fe;                  
                border-radius: 4px;                         
                padding: 14px;
                font-size: 12px;
                font-family: 'Segoe UI', sans-serif;
                font-weight: 800;
                text-transform: uppercase;
                letter-spacing: 1px;                        
            }
            QPushButton:hover {
                background-color: #00f2fe;                  
                color: #05070f;                             
                border: 2px solid #00f2fe;
            }
            QPushButton:pressed {
                background-color: #00b8c4;
                border: 2px solid #00b8c4;
            }
                         
            QFrame#card_inputs, QFrame#card_resultado {
                background-color: #0b0f19;
                border-radius: 12px;
                border: 1px solid #1e293b;
            }
        """)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(40, 40, 40, 40)
        self.main_layout.setSpacing(40)
        
        # ------------------ PAINEL ESQUERDO (INPUTS) ------------------
        self.layout_esquerdo = QVBoxLayout()
        self.main_layout.addLayout(self.layout_esquerdo, stretch=1)
        
        self.card_inputs = QFrame()
        self.card_inputs.setObjectName("card_inputs")
        self.card_inputs_layout = QVBoxLayout(self.card_inputs)
        self.card_inputs_layout.setContentsMargins(40, 40, 40, 40)
        self.card_inputs_layout.setSpacing(15) # Spacing um pouco menor já que o bloco vertical cuida do alinhamento
        
        titulo_inputs = QLabel("Dados da Simulação")
        titulo_inputs.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        titulo_inputs.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo_inputs.setStyleSheet("color: #ffffff; margin-bottom: 10px; letter-spacing: 0.5px; font-weight: 800;")
        self.card_inputs_layout.addWidget(titulo_inputs)
        
        # Ajuste estratégico: Unidades no próprio placeholder/label e alinhamento em bloco vertical
        self.input_capital = self.criar_campo_entrada("CAPITAL INICIAL", "R$ 0,00", self.card_inputs_layout, real=True)
        self.input_aporte = self.criar_campo_entrada("APORTE MENSAL", "R$ 0,00", self.card_inputs_layout, real=True)
        self.input_taxa = self.criar_campo_entrada("TAXA DE JUROS ANUAL (%)", "0.00", self.card_inputs_layout, real=True)
        self.input_inflacao = self.criar_campo_entrada("TAXA DE INFLAÇÃO ANUAL (%)", "0.00", self.card_inputs_layout, real=True)
        self.input_tempo = self.criar_campo_entrada("PERÍODO DE TEMPO (OPCIONAL PARA ALVO)", "Meses desejados", self.card_inputs_layout, real=False)
        self.input_alvo = self.criar_campo_entrada("VALOR ALVO DESEJADO (OPCIONAL)", "Quanto quer acumular em poder de compra?", self.card_inputs_layout, real=True)
        
        layout_botoes = QHBoxLayout()
        layout_botoes.setSpacing(15)
        layout_botoes.setContentsMargins(0, 15, 0, 0)
        
        self.botao_calcular = QPushButton("Simular por Tempo")
        self.botao_calcular.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_calcular.clicked.connect(self.processar_simulacao)
        layout_botoes.addWidget(self.botao_calcular)
        
        self.botao_alvo = QPushButton("Calcular para Alvo")
        self.botao_alvo.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_alvo.clicked.connect(self.processar_simulacao_alvo)
        layout_botoes.addWidget(self.botao_alvo)
        
        self.card_inputs_layout.addLayout(layout_botoes)
        self.layout_esquerdo.addWidget(self.card_inputs)
        
        # ------------------ PAINEL DIREITO (RESULTADOS) ------------------
        self.layout_direito = QVBoxLayout()
        self.main_layout.addLayout(self.layout_direito, stretch=1)
        
        self.card_resultado = QFrame()
        self.card_resultado.setObjectName("card_resultado")
        self.card_layout = QVBoxLayout(self.card_resultado)
        self.card_layout.setContentsMargins(40, 40, 40, 40)
        self.card_layout.setSpacing(22) 
        
        titulo_resultados = QLabel("Projeção de Rendimento")
        titulo_resultados.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        titulo_resultados.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo_resultados.setStyleSheet("color: #ffffff; margin-bottom: 15px; letter-spacing: 0.5px; font-weight: 800;")
        self.card_layout.addWidget(titulo_resultados)
        
        self.lbl_total_investido = self.criar_campo_resultado("Total Investido")
        self.lbl_total_juros = self.criar_campo_resultado("Rendimentos Brutos")
        self.lbl_montante_final = self.criar_campo_resultado("Montante Acumulado")
        self.lbl_compra_real = self.criar_campo_resultado("Poder de Compra Real")
                 
        divisor = QFrame()
        divisor.setFrameShape(QFrame.Shape.HLine)
        divisor.setStyleSheet("background-color: #1e293b; max-height: 1px; margin: 10px 0px;")
        self.card_layout.addWidget(divisor)
        
        self.lbl_poder_compra_titulo = QLabel("Poder de Compra Real\n(Ajustado à Inflação)")
        self.lbl_poder_compra_titulo.setStyleSheet("color: #475569; font-weight: 700; font-size: 11px; text-transform: uppercase; letter-spacing: 1px;")
        
        self.lbl_poder_compra = QLabel("R$ 0,00")
        self.lbl_poder_compra.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        self.lbl_poder_compra.setStyleSheet("color: #00f2fe;")
        
        container_resultado_final = QHBoxLayout()
        container_resultado_final.addWidget(self.lbl_poder_compra_titulo)
        container_resultado_final.addStretch()
        container_resultado_final.addWidget(self.lbl_poder_compra)
        self.card_layout.addLayout(container_resultado_final)
        
        self.card_layout.addStretch()
        self.layout_direito.addWidget(self.card_resultado)
        self.layout_direito.addStretch()

    def criar_campo_entrada(self, label_text, placeholder, layout_destino, real=True):
        # MUDANÇA CRUCIAL: Agora usamos layout VERTICAL para empilhar o texto e o input.
        container_bloco = QVBoxLayout()
        container_bloco.setSpacing(6) # Espaço sutil entre o rótulo e a caixa de texto
        container_bloco.setContentsMargins(0, 2, 0, 2)
                 
        label = QLabel(label_text)
        label.setStyleSheet("""
            font-weight: 700; 
            color: #475569; 
            font-size: 10px; 
            text-transform: uppercase; 
            letter-spacing: 1.2px;
            background: transparent;
        """)
                 
        line_edit = QLineEdit()
        line_edit.setPlaceholderText(placeholder)
        line_edit.setMinimumHeight(44)
                 
        if real:
            validador = QDoubleValidator(0.0, 999999999.0, 2)
            validador.setNotation(QDoubleValidator.Notation.StandardNotation)
            line_edit.setValidator(validador)
        else:
            line_edit.setValidator(QIntValidator(1, 1200))
                     
        container_bloco.addWidget(label)
        container_bloco.addWidget(line_edit)
        layout_destino.addLayout(container_bloco)
        return line_edit
        
    def criar_campo_resultado(self, label_text):
        container = QHBoxLayout()
        lbl_nome = QLabel(label_text)
        lbl_valor = QLabel("R$ 0,00")
                 
        lbl_nome.setStyleSheet("color: #475569; font-weight: 700; font-size: 11px; text-transform: uppercase; letter-spacing: 1px;")
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
            self.lbl_poder_compra_titulo.setText("Poder de Compra Real\n(Ajustado à Inflação)")
            self.lbl_poder_compra.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
            
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
            self.lbl_compra_real.setText(self.formatar_moeda(resultado_calculado.poder_compra_real))
            self.lbl_poder_compra.setText(self.formatar_moeda(resultado_calculado.poder_compra_real))
        except Exception as e:
            QMessageBox.critical(self, "Erro no Cálculo", f"Ocorreu um erro ao processar a simulação: {str(e)}")

    def processar_simulacao_alvo(self):
        try:
            capital = float(self.input_capital.text().replace(",", ".")) if self.input_capital.text() else 0.0
            aporte = float(self.input_aporte.text().replace(",", ".")) if self.input_aporte.text() else 0.0
            taxa = float(self.input_taxa.text().replace(",", ".")) if self.input_taxa.text() else 0.0
            inflacao = float(self.input_inflacao.text().replace(",", ".")) if self.input_inflacao.text() else 0.0
            alvo = float(self.input_alvo.text().replace(",", ".")) if self.input_alvo.text() else 0.0

            if alvo <= 0:
                QMessageBox.warning(self, "Aviso", "Por favor, insira um valor Alvo válido.")
                return
            if alvo <= capital:
                QMessageBox.warning(self, "Aviso", "O valor alvo deve ser maior do que o capital inicial.")
                return
            if taxa <= 0 and aporte <= 0:
                QMessageBox.warning(self, "Aviso", "Insira uma taxa de juros ou um aporte mensal maior que zero.")
                return

            simulador = SimuladorFinanceiro()
            res: ResultadoMeta = simulador.calcular_tempo_ate_alvo(capital, aporte, taxa, inflacao, alvo)
            
            self.lbl_total_investido.setText(self.formatar_moeda(res.total_investido))
            self.lbl_total_juros.setText(self.formatar_moeda(res.total_juros))
            self.lbl_montante_final.setText(self.formatar_moeda(res.montante_final))
            self.lbl_compra_real.setText(self.formatar_moeda(res.poder_compra_real))
            
            self.lbl_poder_compra_titulo.setText("Tempo até atingir o Alvo\n(Descontada a Inflação)")
            self.lbl_poder_compra.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
            self.lbl_poder_compra.setText(res.tempo_texto)
            
        except Exception as e:
            QMessageBox.critical(self, "Erro no Cálculo", f"Ocorreu um erro ao calcular o tempo até o alvo: {str(e)}")