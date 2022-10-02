from PyQt5.QtWidgets import QApplication, QStyleFactory
from ui.totalizador import clasePrincipal

import sys
'''
def run():
    app = QApplication(sys.argv)
    ui = clasePrincipal()
    ui.show()
    #sys.exit(app.exec_())
    app.exec_()
run()
'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fussion')) # won't work on windows style.
    ui = clasePrincipal()
    ui.show()
    app.exec_()

