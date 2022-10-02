# -*- coding: utf-8 -*-

"""
Module implementing clasePrincipal.
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from .uiTotalizador import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QLabel
import os
from os.path import splitext
import gpxpy
import glob

class clasePrincipal(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(clasePrincipal, self).__init__(parent)
        self.setupUi(self)
        self.nTrack = 0
        self.kmAcu = 0
    def anadeLinea(self, *args):
    #def anadeLinea(self, nTrack,fileName, kmTrack, kmCarpeta):
        col = 0
        self.listaTracks.insertRow(self.listaTracks.rowCount())
        for arg in args:            
            item = QtWidgets.QTableWidgetItem(str(arg))
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            self.listaTracks.setItem(self.listaTracks.rowCount()-1, col, item)
            if (col!=1):
                item.setTextAlignment(132) #4--> center, 128 --> Vcenter
            col+=1
        
    @pyqtSlot()
    def on_btnSeleccion_clicked(self):
        """
        Slot documentation goes here.
        """
        global carpeta
        carpeta = QFileDialog.getExistingDirectory(self, 'Selecciona la carpeta') +'/'
        #self.anadeLinea('Se va a procesar la carpeta : {}'.format(carpeta)) 
    
    @pyqtSlot()
    def on_btnProcesar_clicked(self):
        """
        Slot documentation goes here.
        """
        self.nTrack = 0
        self.kmAcu = 0
        processFolder(self, carpeta)
        if self.checkSubcarpetas.isChecked():
            for root, dirs, files in os.walk(carpeta):
                for dir in dirs:
                    folder = os.path.join(root, dir) +'/'
                    processFolder(self, folder)
        linea ='El total acumulado es de : {:.1f} km'.format(self.kmAcu)
        #self.anadeLinea(linea)
        
def processFolder(self, folder):        
        # Si está checked checkStump
        if self.checkFilter.isChecked():            
            ruta = folder + self.linePattern.text()
        else:
            ruta = folder + "*.gpx"
        gpxList = glob.glob(ruta)
        #self.anadeLinea("Se han encontrado {} tracks".format(len(gpxList)))
        print("Se han encontrado {} tracks".format(len(gpxList)))           
        kmCarpeta = 0
        for fileName in gpxList:
            with open(fileName, 'r') as gpx_file:
                gpx = gpxpy.parse(gpx_file)
                for track in gpx.tracks:
                    kmTrack = track.length_3d() / 1000.0 
                    self.kmAcu += kmTrack
                    #linea = "Nombre de archivo: {} -- Longitud: {:5.1f} km -- Acumulado: {:5.1f} km".format(fileName, kmTrack, kmCarpeta)
                    self.nTrack+=1
                    self.anadeLinea(self.nTrack,fileName, "{:5.1f}".format(kmTrack), "{:5.1f}".format(self.kmAcu))
        for i in range(4):
            self.listaTracks.resizeColumnToContents(i)
        
