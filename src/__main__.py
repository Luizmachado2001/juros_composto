# src/main.py
import sys
from PyQt6.QtWidgets import QApplication
from src.ui.main_window import MainWindow

def main():
    # Inicializa o gerenciador da aplicação PyQt6
    app = QApplication(sys.argv)
    
    # Cria a instância da tela que desenhamos
    janela = MainWindow()
    janela.show()
    
    # Mantém a janela aberta em loop até o usuário fechar
    sys.exit(app.exec())

if __name__ == "__main__":
    main()