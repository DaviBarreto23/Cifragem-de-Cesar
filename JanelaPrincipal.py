from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout


class MainWindows(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.central_widget = QWidget()
        self.grid_Layout = QVBoxLayout()
        self.central_widget.setLayout(self.grid_Layout)
        self.setCentralWidget(self.central_widget)
        self.setStyleSheet(
            """
       background-color: rgb(15, 6, 6);
        color: #FFFFFF;
        font-family: Titillium;
        font-size: 18px;
        """
        )

        self.setWindowTitle('cifragem de César')

    def ajustefixo(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addwidgetToLayout(self, widget: QWidget):
        self.grid_Layout.addWidget(widget)
