# -*- coding: utf-8 -*-

"""
Module implementing clasePrincipal.
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from .Ui_totalizadorKm import Ui_MainWindow
import os
from os.path import splitext
import gpxpy

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
    def anadeLinea(self, linea):
        self.listaTracks.addItem(linea)     
    @pyqtSlot()
    def on_btnSeleccion_clicked(self):
        """
        Slot documentation goes here.
        """
        global carpeta
        carpeta = QFileDialog.getExistingDirectory(self, 'Selecciona la carpeta') +'/'
        self.anadeLinea('Se va a procesar la carpeta : {}'.format(carpeta)) 
    
    @pyqtSlot()
    def on_btnProcesar_clicked(self):
        """
        Slot documentation goes here.
        """
        kmAcumulados = 0
        # First process initial folder
        kmAcumulados += processFolder(self, carpeta) 
        # If selected, traverse down all folders from iniPath
        if self.checkSubcarpetas.isChecked():
            for root, dirs, files in os.walk(carpeta):
                for dir in dirs:
                    folder = os.path.join(root, dir) +'/'
                    kmAcumulados += processFolder(self, folder)
        linea ='El total acumulado es de : {:.1f} km'.format(kmAcumulados)
        self.anadeLinea(linea)
        
def processFolder(self, folder):
        gpxList = [x for x in os.listdir(folder) if splitext(x)[1].lower() in {'.gpx'}]
        print("Se han encontrado {} tracks".format(len(gpxList)))
        kmCarpeta = 0
        for fileName in gpxList:
            with open(folder+fileName, 'r') as gpx_file:
                gpx = gpxpy.parse(gpx_file)
                for track in gpx.tracks:
                    kmTrack = track.length_3d() / 1000.0 
                    kmCarpeta += kmTrack 
                    linea = "Nombre de archivo: {} -- Longitud: {:5.1f} km -- Acumulado: {:5.1f} km".format(fileName, kmTrack, kmCarpeta)
                    self.anadeLinea(linea)                    
        return kmCarpeta 
