from PySide6.QtWidgets import QTextEdit
from PySide6.QtCore import Qt


class Display(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    # função para alinhar a direita do display

    def configStyle(self):
        self.setStyleSheet(self.setMinimumHeight(150))
        self.setStyleSheet(self.setMinimumWidth(500))
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setStyleSheet(
            """
        background-color:rgb(85, 1, 1);
        color: #FFFFFF;
        font-family: Titillium;
        font-size: 20px;
        """
        )
