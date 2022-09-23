import os
import gpxpy
from os.path import splitext
def procesaCarpeta():    
    gpxList = [x for x in os.listdir('../RUTAS/tracks/') if splitext(x)[1].lower() in {'.gpx'}]
    print("Se han encontrado {} tracks".format(len(gpxList)))
    kilometrada = 0
    for fileName in gpxList:
        with open('../RUTAS/tracks/'+fileName, 'r') as gpx_file:
            gpx = gpxpy.parse(gpx_file)
            for track in gpx.tracks:
                kilometrada += track.length_3d()
                print("Nombre de archivo: {} -- Longitud: {:5.1f} km -- Acumulado: {:5.1f} km".format(fileName, track.length_3d()/1000, kilometrada/1000))
    return kilometrada
            
print('Total de km acumulados: {}'.format(int(procesaCarpeta()/1000)))            