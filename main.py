# coding=utf-8
from dataReader import *
from Sensors import *
from Sample import *
from LearningSet import *
from knnGesto import *
from knnMove import *
from RecoverySet import *
from knnIdeograma import *
import glob, random, time

porcentaje = 90

samples = list()
ls = LearningSet()
rs = RecoverySet()
objKnnGesto = knnGesto()
objKnnMove = knnMove()
objKnnIdeograma = knnIdeograma()
#startLearning = time.time()
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

    #print(sensores.getClass())
    sample.setClass(sensores.getClass())
    sample.standardDeviation(sensores.getEmg())
    sample.segmentation(sensores.getVector('ax'), 'ax')
    sample.segmentation(sensores.getVector('ay'), 'ay')
    sample.segmentation(sensores.getVector('az'), 'az')
    print (row, len(sample.getSegmentX()), len(sample.getSegmentY()), len(sample.getSegmentZ()))

    samples.append(sample)

    del sensores
    del sample

i = float(len(samples))/100
random.shuffle(samples)

ls.setValues(samples[:int(i*porcentaje)])
rs.setValues(samples[int(i*porcentaje):])

"""print(ls.getValues())
print(rs.getValues())
for row in samples[:int(i*80)]:
    print (row.getClass())
print("*"*10)
for row in samples[int(i*80):]:
    print(row.getClass())"""

objKnnGesto.learning(ls.getValues())
objKnnMove.learning(ls.getValues())

lsIdeogramas = list()

for sample in samples[:int(i*porcentaje)]:
    id_gesto = objKnnGesto.recovery(sample)
    id_move = objKnnMove.recovery(sample)
    #print (sample.getClass(), id_move, id_gesto)
    lsIdeogramas.append([sample.getClass(), int(id_gesto), int(id_move)])

objKnnIdeograma.learning(lsIdeogramas)
#endLearning = time.time()

count = 0
for sample in rs.getValues():
    startMuestra = time.time()
    id_gesto = objKnnGesto.recovery(sample)
    id_move = objKnnMove.recovery(sample)
    nameIdeograma = objKnnIdeograma.recovery([int(id_gesto), int(id_move)])
    endMuestra = time.time()
    print('Muestra:', endMuestra - startMuestra)
    #print (nameIdeograma, sample.getClass(), nameIdeograma == sample.getClass())
    if nameIdeograma == sample.getClass():
        count = count + 1
print(count, len(rs.getValues()))
print('Efectividad:', (count*100)/len(rs.getValues()))
#print('Aprendizaje:', endLearning - startLearning)
