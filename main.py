from PyQt5.QtWidgets import QApplication
from ui.totalizadorKm import clasePrincipal

import sys

def run():
    app = QApplication(sys.argv)
    ui = clasePrincipal()
    ui.show()
    #sys.exit(app.exec_())
    app.exec_()
run()
