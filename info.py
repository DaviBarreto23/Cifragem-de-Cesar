from PySide6.QtWidgets import QLabel, QWidget, QTextEdit
from PySide6.QtCore import Qt


class Info(QTextEdit):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.configStyle()

    def configStyle(self):
        self.setPlaceholderText('Resultado')
        # self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setStyleSheet(self.setMinimumHeight(150))
        self.setStyleSheet(self.setMinimumWidth(500))
        self.setStyleSheet(
            """
        background-color:rgb(85, 1, 1);
        color: #FFFFFF;
        font-family: Titillium;
        font-size: 20px;
        """
        )
