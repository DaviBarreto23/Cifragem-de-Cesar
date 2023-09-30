from PySide6.QtWidgets import QPushButton, QGridLayout, QLineEdit
from PySide6.QtCore import Slot
from display import Display
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from info import Info


class Botao(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        fonte = self.font()
        fonte.setBold(True)
        # tem que colocar  setFont para que os de cima funcione no botão
        self.setFont(fonte)
        self.setStyleSheet(
            """
        background-color: rgb(224, 4, 4);
         color: rgb(255, 255, 255);
        font-family: Titillium;
        font-size: 20px;
        """
        )


class GridDeBotoes(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._mascaraGride = [
            ['cifrar', 'decifrar', 'limpar'],
        ]
        self.info = info
        self.display = display
        self.equation = ''
        self._facaGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, valor):
        self._equation = valor
        self.info.setText(valor)

    def _facaGrid(self):
        for numeroLinha, dadoslinha in enumerate(self._mascaraGride):
            for numeroColuna, textoBotao in enumerate(dadoslinha):
                botao = Botao(textoBotao)

                self.addWidget(botao, numeroLinha, numeroColuna)
                slot = self._facaBotaoNoDisplay(
                    self._inserirTextodoBotaoNoDisplay, botao
                )
                self._conectaBotaoClique(botao, slot)
                self._configurarBotaoEspecial(botao)

    def _conectaBotaoClique(self, botao, slot):
        botao.clicked.connect(slot)

    def _configurarBotaoEspecial(self, botao):
        texto = botao.text()
        if texto == 'limpar':
            # primeira forma de fazer o clear no botão limpar
            # slot = self._facaBotaoNoDisplay(self.display.clear)
            # self._conectaBotaoClique(botao, slot)

            # segunda forma de fazer o clear no botão limpar
            # botao.clicked.connect(self.display.clear)

            self._conectaBotaoClique(botao, self._Limpar)

        if texto == 'cifrar':
            self._conectaBotaoClique(botao, self._cifratela)
        if texto == 'decifrar':
            self._conectaBotaoClique(botao, self._deciTela)

    def _facaBotaoNoDisplay(self, funcao, *args, **kwargs):
        @Slot()
        def Slotreal():
            funcao(*args, **kwargs)
        return Slotreal

    def _inserirTextodoBotaoNoDisplay(self, botao):
        texto_botao = botao.text()
        self.display.insertPlainText(texto_botao)

    def _Limpar(self):
        self.display.clear()

    def _cifratela(self):
        cifragem = ''
        textoDisplay = self.display.toPlainText().removesuffix('cifrar')
        for cf in textoDisplay:
            if cf in 'Aa':
                cifragem = cifragem + 'D'
            elif cf in 'Bb':
                cifragem = cifragem + 'E'
            elif cf in 'Cc':
                cifragem = cifragem + 'F'
            elif cf in 'Dd':
                cifragem = cifragem + 'G'
            elif cf in 'Ee':
                cifragem = cifragem + 'H'
            # criptografia do E com acento agudo e circunflexo
            # elif cf in 'Éé':
            #     cifragem += '/'
            # elif cf in 'Êê':
            #     cifragem += '?'
            elif cf in 'Ff':
                cifragem = cifragem + 'I'
            elif cf in 'Gg':
                cifragem = cifragem + 'J'
            elif cf in 'Hh':
                cifragem = cifragem + 'K'
            elif cf in 'Ii':
                cifragem = cifragem + 'L'
            elif cf in 'Jj':
                cifragem = cifragem + 'M'
            elif cf in 'Kk':
                cifragem = cifragem + 'N'
            elif cf in 'Ll':
                cifragem = cifragem + 'O'
            elif cf in 'Mm':
                cifragem += 'P'
            elif cf in 'Nn':
                cifragem += 'Q'
            elif cf in 'Oo':
                cifragem += 'R'
            elif cf in 'Pp':
                cifragem += 'S'
            elif cf in 'Qq':
                cifragem += 'T'
            elif cf in 'Rr':
                cifragem += 'U'
            elif cf in 'Ss':
                cifragem += 'V'
            elif cf in 'Tt':
                cifragem += 'W'
            elif cf in 'Uu':
                cifragem += 'X'
            elif cf in 'Vv':
                cifragem += 'Y'
            elif cf in 'Ww':
                cifragem += 'Z'
            elif cf in 'Xx':
                cifragem += 'A'
            elif cf in 'Yy':
                cifragem += 'B'
            elif cf in 'Zz':
                cifragem += 'C'
            else:
                cifragem = cifragem + cf

        self.display.clear()
        self.equation = cifragem

    def _deciTela(self):
        decifragem = ''
        textoDisplay = self.display.toPlainText().removesuffix('decifrar')
        for df in textoDisplay:
            if df in 'Dd':
                decifragem += 'A'
            elif df in 'Ee':
                decifragem += 'B'
            elif df in 'Ff':
                decifragem += 'C'
            elif df in 'Gg':
                decifragem += 'D'
            elif df in 'Hh':
                decifragem += 'E'
            elif df in 'Ii':
                decifragem += 'F'
            elif df in 'Jj':
                decifragem += 'G'
            elif df in 'Kk':
                decifragem += 'H'
            elif df in 'Ll':
                decifragem += 'I'
            elif df in 'Mm':
                decifragem += 'J'
            elif df in 'Nn':
                decifragem += 'K'
            elif df in 'Oo':
                decifragem += 'L'
            elif df in 'Pp':
                decifragem += 'M'
            elif df in 'Qq':
                decifragem += 'N'
            elif df in 'Rr':
                decifragem += 'O'
            elif df in 'Ss':
                decifragem += 'P'
            elif df in 'Tt':
                decifragem += 'Q'
            elif df in 'Uu':
                decifragem += 'R'
            elif df in 'Vv':
                decifragem += 'S'
            elif df in 'Ww':
                decifragem += 'T'
            elif df in 'Xx':
                decifragem += 'U'
            elif df in 'Yy':
                decifragem += 'V'
            elif df in 'Zz':
                decifragem += 'W'
            elif df in 'Aa':
                decifragem += 'X'
            elif df in 'Bb':
                decifragem += 'Yy'
            elif df in 'Cc':
                decifragem += 'Zz'
            else:
                decifragem += df
        self.display.clear()
        self.equation = decifragem
