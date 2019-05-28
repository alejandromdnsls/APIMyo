# coding=utf-8
import glob, sys, os

cad = 'Nuevo\\*' + sys.argv[1] + '_*.csv'
listOfFiles = glob.glob(cad)

for archivo in listOfFiles:
    if sys.argv[1] in archivo:
        #print archivo.split('\\')[0] + '\\' + sys.argv[1] + '\\' + archivo.split('\\')[1]
        os.rename(archivo, archivo.split('\\')[0] + '\\' + sys.argv[1] + '\\' + archivo.split('\\')[1])
