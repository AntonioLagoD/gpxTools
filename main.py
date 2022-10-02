from PyQt5.QtWidgets import QApplication, QStyleFactory
from ui.totalizador import clasePrincipal

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fussion'))
    ui = clasePrincipal()
    ui.show()
    app.exec_()

