# coding=utf-8
from dataReader import *
from Sensors import *
from Sample import *
from LearningSet import *
from knnGesto import *
from knnMove import *
from RecoverySet import *
from knnIdeograma import *
import glob, random

kfold = 309

samples = list()
objKnnGesto = knnGesto()
objKnnMove = knnMove()
objKnnIdeograma = knnIdeograma()
sets = list()
eficiencia = list()
eficienciaGesto = list()
eficienciaMovimiento = list()
archivos = glob.glob("Datos\\MuestraNuevo\\*.xlsx")

for row in archivos:
    sensores = Sensors()
    sample = Sample()
    data = dataReader(row)

    sensores.setClass(row.split('.')[0].split('\\')[-1].split('_')[0])
    sensores.setVector('ax', data.read()[0])
    sensores.setVector('ay', data.read()[1])
    sensores.setVector('az', data.read()[2])
    sensores.setVector('emg1', data.read()[3])
    sensores.setVector('emg2', data.read()[4])
    sensores.setVector('emg3', data.read()[5])
    sensores.setVector('emg4', data.read()[6])
    sensores.setVector('emg5', data.read()[7])
    sensores.setVector('emg6', data.read()[8])
    sensores.setVector('emg7', data.read()[9])
    sensores.setVector('emg8', data.read()[10])

    sample.setClass(sensores.getClass())
    sample.standardDeviation(sensores.getEmg())
    sample.segmentation(sensores.getVector('ax'), 'ax')
    sample.segmentation(sensores.getVector('ay'), 'ay')
    sample.segmentation(sensores.getVector('az'), 'az')

    #print (row, len(sample.getSegmentX()), len(sample.getSegmentY()), len(sample.getSegmentZ()))

    samples.append(sample)

    del sensores
    del sample

random.shuffle(samples)
val = len(archivos)/kfold
for index in range(kfold):
    sets.append(samples[int(val*index):int((index+1)*val)])

for row in range(len(sets)):
    ls = LearningSet()
    rs = RecoverySet()
    out = list()
    aux = sets[row]
    aux1 = sets[:row] + sets[row + 1:]
    for i in aux1:
        for val in i:
            out.append(val)
    ls.setValues(out)
    rs.setValues(aux)
    objKnnGesto.learning(ls.getValues())
    objKnnMove.learning(ls.getValues())

    lsIdeogramas = list()

    for sample in out:
        id_gesto = objKnnGesto.recovery(sample)
        id_move = objKnnMove.recovery(sample)
        lsIdeogramas.append([sample.getClass(), int(id_gesto), int(id_move)])

    objKnnIdeograma.learning(lsIdeogramas)

    count = 0
    countGesto = 0
    countMove = 0
    for sample in rs.getValues():
        id_gesto = objKnnGesto.recovery(sample)
        nameGesto = objKnnGesto.recClass(sample)
        id_move = objKnnMove.recovery(sample)
        nameMove = objKnnMove.recClass(sample)
        nameIdeograma = objKnnIdeograma.recovery([int(id_gesto), int(id_move)])
        #print (nameIdeograma, sample.getClass(), nameIdeograma == sample.getClass())
        if nameIdeograma == sample.getClass():
            count = count + 1
        if nameGesto == sample.getClass():
            countGesto = countGesto + 1
        if nameMove == sample.getClass():
            countMove = countMove + 1
    #print(count, len(rs.getValues()))
    #print('Efectividad:', (count*100)/len(rs.getValues()))
    eficiencia.append((count*100)/len(rs.getValues()))
    eficienciaGesto.append((countGesto*100)/len(rs.getValues()))
    eficienciaMovimiento.append((countMove*100)/len(rs.getValues()))
    del rs
    del ls

total = 0
for val in eficiencia:
    total = total + val
totalMove = 0
for val in eficienciaMovimiento:
    totalMove = totalMove + val
totalGesto = 0
for val in eficienciaGesto:
    totalGesto = totalGesto + val
print('Total Gesto:', totalGesto/len(eficiencia))
print('Total Movimiento:', totalMove/len(eficiencia))
print('Total ideogramas:', total/len(eficiencia))
