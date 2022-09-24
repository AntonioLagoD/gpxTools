# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/mnt/DATOS/Arduino/proyectos/gpxTools/ui/totalizadorKm.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listaTracks = QtWidgets.QListWidget(self.centralwidget)
        self.listaTracks.setGeometry(QtCore.QRect(10, 10, 1180, 720))
        self.listaTracks.setObjectName("listaTracks")
        self.listaTracks.setAlternatingRowColors(True)
        self.listaTracks.setStyleSheet("font: 12pt Arial")
        self.btnSeleccion = QtWidgets.QPushButton(self.centralwidget)
        self.btnSeleccion.setGeometry(QtCore.QRect(90, 740, 260, 40))
        self.btnSeleccion.setObjectName("btnSeleccion")
        self.btnProcesar = QtWidgets.QPushButton(self.centralwidget)
        self.btnProcesar.setGeometry(QtCore.QRect(800, 740, 260, 40))
        self.btnProcesar.setObjectName("btnProcesar")
        self.checkSubcarpetas = QtWidgets.QCheckBox(self.centralwidget)
        self.checkSubcarpetas.setGeometry(QtCore.QRect(370, 740, 170, 40))
        self.checkSubcarpetas.setObjectName("checkSubcarpetas")
        self.checkFilter = QtWidgets.QCheckBox(self.centralwidget)
        self.checkFilter.setEnabled(True)
        self.checkFilter.setGeometry(QtCore.QRect(500, 740, 111, 40))
        self.checkFilter.setObjectName("checkFilter")
        self.linePattern = QtWidgets.QLineEdit(self.centralwidget)
        self.linePattern.setGeometry(QtCore.QRect(610, 750, 171, 20))
        self.linePattern.setObjectName("linePattern")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Totalizador de km"))
        self.btnSeleccion.setText(_translate("MainWindow", "Seleccionar Carpeta"))
        self.btnProcesar.setText(_translate("MainWindow", "Procesar Carpeta(s)"))
        self.checkSubcarpetas.setText(_translate("MainWindow", "Procesar subcarpetas"))
        self.checkFilter.setText(_translate("MainWindow", "Filtrar por patrón : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
