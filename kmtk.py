import os
from tkinter import filedialog
from tkinter import *
from os.path import splitext
import gpxpy

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print (filename)

def process():
    kmAcumulados = 0
    iniPath = folder_path.get()+'/'
    # First process initial folder
    kmAcumulados += processFolder(iniPath) 
    # If selected, traverse down all folders from iniPath
    if (recurs.get()==1):
        for root, dirs, files in os.walk(iniPath):
            for dir in dirs:
                folder = os.path.join(root, dir) +'/'
                kmAcumulados += processFolder(folder)
    print('El total acumulado es de : {:.1f} km'.format(kmAcumulados))
    resultado.configure(text='Total acumulado: {:.1f} km'.format(kmAcumulados))
def processFolder(folder):
    gpxList = [x for x in os.listdir(folder) if splitext(x)[1].lower() in {'.gpx'}]
    print("Se han encontrado {} tracks".format(len(gpxList)))
    kmCarpeta = 0
    for fileName in gpxList:
        with open(folder+fileName, 'r') as gpx_file:
            gpx = gpxpy.parse(gpx_file)
            for track in gpx.tracks:
                kmTrack = track.length_3d() / 1000.0 
                kmCarpeta += kmTrack 
                print("Nombre de archivo: {} -- Longitud: {:5.1f} km -- Acumulado: {:5.1f} km".format(fileName, kmTrack, kmCarpeta))
    return kmCarpeta    
  
    
window = Tk()
window.title("Análisis de kilometraje de rutas")
folder_path = StringVar()
recurs = IntVar()
folder_path.set("Carpeta : ")
statustxt = StringVar()
button1 = Button(text="Seleccionar carpeta", command=browse_button, height = 2, width = 50)
button1.grid(row=1, sticky=W+E)
button2 = Button(text="Procesar", command=process, height = 2, width = 10)
button2.grid(row=2, sticky=W+E)
#button3 = Button(text="UPLOAD", command=upload, height = 2, width = 10)
#button3.grid(row=3, sticky=W+E)
Checkbutton(window, text="Procesar subcarpetas", variable=recurs).grid(row=4, sticky=W)

lbl1 = Label(master=window,textvariable=folder_path,anchor="w")
lbl1.grid(row=10, sticky=W)
resultado = Label(master=window,text='Total acumulado: ---',anchor="w")
resultado.grid(row=11, sticky=W+E)
window.geometry(u'1200x800')
mainloop()
