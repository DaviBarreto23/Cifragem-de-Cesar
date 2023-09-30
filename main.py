from PySide6.QtWidgets import QApplication
from JanelaPrincipal import MainWindows
from display import Display
from botoes import GridDeBotoes
from info import Info
from PySide6.QtGui import QIcon
from variaveis import WINDOW_ICON_PATH

import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindows()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    display = Display()
    display.setPlaceholderText('Digite para cifrar ou decifrar')
    window.addwidgetToLayout(display)

    info = Info()
    window.addwidgetToLayout(info)

    # botao = Botao('cifrar')
    # window.addwidgetToLayout(botao)
    # botao_2 = Botao('decifrar')
    # window.addwidgetToLayout(botao_2)
    # window.ajustefixo()
    botaogrid = GridDeBotoes(display, info)
    window.grid_Layout.addLayout(botaogrid)
    window.show()
    app.exec()
